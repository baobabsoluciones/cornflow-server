from cornflow_client import CornFlow, CornFlowApiError, SchemaManager
from airflow import AirflowException
from airflow.secrets.environment_variables import EnvironmentVariablesBackend
from urllib.parse import urlparse
import json
import os

# TODO: move these functions to cornflow client

def get_arg(arg, context):
    """
    Get an argument from the kwargs given to a task
    
    :param arg: The name fo the argument (string)
    :param context: The list of kwargs
    :return: The argument value.
    """
    return context["dag_run"].conf[arg]


def get_requirements(path):
    """
    Read requirements.txt from a project and return a list of packages.
    
    :param path: The path of the project
    :return: A list of required packages
    """
    req_path = path + "/requirements.txt"
    
    try:
        with open(req_path, "r") as file:
            req_list = file.read().splitlines()
    except:
        print("no requirement file in this path")
        return []
    
    return req_list


def connect_to_cornflow():
    """
    Create a connection to cornflow and log in with airflow admin user.
    
    :return: A logged and connected Cornflow class instance
    """
    # This secret comes from airflow configuration
    print("Getting connection information from ENV VAR=CF_URI")
    secrets = EnvironmentVariablesBackend()
    uri = secrets.get_conn_uri('CF_URI')
    conn = urlparse(uri)
    # TODO: what if https??
    url="http://{}:{}".format(conn.hostname, conn.port)

    airflow_user = CornFlow(url=url)
    airflow_user.login(email=conn.username, pwd=conn.password)
    return airflow_user


def cf_get_data(client, kwargs):
    """
    Connect to cornflow and ask for the input data corresponding to the execution id.
    
    :param kwargs: kwargs passed to the dag task.
    :return: A logged and connected Cornflow class instance, the input data, the input config.
    """
    exec_id = get_arg("exec_id", kwargs)
    
    # login
    # airflow_user = connect_to_cornflow()
    print("starting to solve the model with execution %s" % exec_id)
    # get data
    execution_data = client.get_data(exec_id)
    
    return execution_data["data"], execution_data["config"]


def try_to_save_error(client, exec_id, state=-1):
    try:
        client.put_api_for_id('dag/', id=exec_id, payload=dict(state=state))
    except Exception as e:
        print("An exception trying to register the failed status: {}".format(e))


def cf_solve(fun, dag_name, **kwargs):
    """
    Connect to cornflow, ask for data, solve the problem and write the solution in cornflow
    
    :param fun: The function to use to solve the problem.
    :param dag_name: the name of the dag, to later search the output schema
    :param kwargs: other kwargs passed to the dag task.
    :return:
    """
    exec_id = get_arg("exec_id", kwargs)
    client = connect_to_cornflow()
    data, config = cf_get_data(client, kwargs = kwargs)
    try:
        solution, log, log_json = fun(data, config)
    except NoSolverException as e:
        try_to_save_error(client, exec_id, -1)
        raise AirflowException(e)
    except Exception as e:
        try_to_save_error(client, exec_id, -1)
        raise AirflowException('There was an error during the solving')
    try:

        _file = os.path.join(os.path.dirname(__file__),
                             "{}_output.json".format(dag_name))
        with open(_file, 'r') as f:
            schema = json.load(f)
    except:
        try_to_save_error(client, exec_id, -1)
        raise AirflowException('Error while loading solution schema')
    if solution:
        # we check if the solution is compatible with the schema.
        # If it's not: we change the status to Invalid
        # and take out the server validation of the schema\
        # TODO: not sure if this idea makes sense
        marshmallow_obj = SchemaManager(schema).jsonschema_to_flask()
        data = marshmallow_obj().load(solution)
        if data is None:
            log_json['status'] = 'Invalid'
            dag_name = None
        payload = dict(data = solution, log_json=log_json, log_text=log,
                       solution_schema = dag_name, state=1)
    else:
        payload = dict(state = 1, log_json=log_json, log_text=log,
                       solution_schema = dag_name)
    
    # Send the solution to cornflow.
    try:
        client.write_solution(execution_id=exec_id, **payload)
    except CornFlowApiError:
        try_to_save_error(client, exec_id, -6)
        # attempt to update the execution with a failed status.
        raise AirflowException('The writing of the solution failed')


    if solution:
        return "Solution saved"


class NoSolverException(Exception):
    pass