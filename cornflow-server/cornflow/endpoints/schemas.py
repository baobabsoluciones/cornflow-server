"""
Endpoints to get the schemas
"""

# Import from libraries
from cornflow_client.airflow.api import Airflow
from flask import current_app, request
from flask_apispec import marshal_with, doc
import logging as log
from cornflow_core.authentication import authenticate

# Import from internal modules
from ..models import PermissionsDAG, DeployedDAG
from ..shared.authentication import Auth
from cornflow_core.exceptions import AirflowError, NoPermission
from ..schemas.schemas import SchemaOneApp, SchemaListApp
from cornflow_core.resources import BaseMetaResource

from ..shared.const import ALL_DEFAULT_ROLES


class SchemaEndpoint(BaseMetaResource):
    """
    Endpoint used to obtain names of available apps
    """

    ROLES_WITH_ACCESS = ALL_DEFAULT_ROLES

    @doc(description="Get list of available apps", tags=["Schemas"])
    @authenticate(auth_class=Auth())
    @marshal_with(SchemaListApp(many=True))
    def get(self):
        """
        API method to get a list of dag names

        :return: A dictionary with a message and a integer with the HTTP status code
        :rtype: Tuple(dict, integer)
        """
        user = Auth().get_user_from_header(request.headers)
        dags = PermissionsDAG.get_user_dag_permissions(user.id)
        available_dags = [{"name": dag.dag_id} for dag in dags]

        log.info("User gets list of schema")
        return available_dags


class SchemaDetailsEndpoint(BaseMetaResource):
    """
    Endpoint used to obtain schemas for one app
    """

    ROLES_WITH_ACCESS = ALL_DEFAULT_ROLES

    @doc(description="Get instance, solution and config schema", tags=["Schemas"])
    @authenticate(auth_class=Auth())
    @marshal_with(SchemaOneApp)
    def get(self, dag_name):
        """
        API method to get the input, output and config schemas for a given dag

        :return: A dictionary with a message and a integer with the HTTP status code
        :rtype: Tuple(dict, integer)
        """
        user = Auth().get_user_from_header(request.headers)
        permission = PermissionsDAG.check_if_has_permissions(
            user_id=user.id, dag_id=dag_name
        )

        if permission:
            deployed_dag = DeployedDAG.get_one_object(dag_name)
            return {
                "instance": deployed_dag.instance_schema,
                "solution": deployed_dag.solution_schema,
                "config": deployed_dag.config_schema
            }, 200
        else:
            raise NoPermission(
                error="User does not have permission to access this dag",
                status_code=403,
            )
