from airflow_config.dags.cornflow_api import CornFlow

email = 'some_email@gmail.com'
pwd = 'some_password'
name = 'some_name'

config = dict(email=email, pwd=pwd, name=name)

client = CornFlow(url="http://127.0.0.1:5000")
client.sign_up(**config)
client.login(email, pwd)

import pulp
prob = pulp.LpProblem("test_export_dict_MIP", pulp.LpMinimize)
x = pulp.LpVariable("x", 0, 4)
y = pulp.LpVariable("y", -1, 1)
z = pulp.LpVariable("z", 0, None, pulp.LpInteger)
prob += x + 4 * y + 9 * z, "obj"
prob += x + y <= 5, "c1"
prob += x + z >= 10, "c2"
prob += -y + z == 7.5, "c3"
data = prob.to_dict()

instance_id = client.create_instance(data)

config = dict(
    solver="PULP_CBC_CMD",
    mip=True,
    msg=True,
    warmStart=True,
    timeLimit=10,
    options=["donotexist", "thisdoesnotexist"],
    keepFiles=0,
    gapRel=0.1,
    gapAbs=1,
    threads=1,
    logPath="test_export_solver_json.log"
)
execution_id = '1b06da8e5c670ba715fbe7f04f8538a687b900bb'
execution_id = client.create_execution(instance_id, config)
status = client.get_status(execution_id)
results = client.get_results(execution_id)
results.keys()
_vars, prob = pulp.LpProblem.from_dict(results['execution_results'])

# get the values for the variables:
{k: v.value() for k, v in _vars.items()}

# get the log in text format
results['log_text']

# get the log in json format
results['log_json']
