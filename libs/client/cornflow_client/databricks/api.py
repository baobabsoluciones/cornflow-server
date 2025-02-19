"""
Python class to implement the Databricks client wrapper
"""

import logging
import requests
from databricks.sdk import WorkspaceClient

from cornflow_client.orchestrator_constants import config_orchestrator

# TODO AGA: CODIGO REPETIDO
# TODO AGA: revisar si el import está bien
from cornflow_client.constants import DatabricksError

logger = logging.getLogger("")


class Databricks:
    def __init__(self, url, token):
        self.url = f"https://adb-3109346743730783.3.azuredatabricks.net"
        self.client = WorkspaceClient(host=url, token=token)
        self.constants = config_orchestrator["databricks"]
        self.token = token

    @classmethod
    def from_config(cls, config):
        data = dict(
            url=config["DATABRICKS_URL"],
            token=config["DATABRICKS_TOKEN"],
        )
        return cls(**data)

    def is_alive(self):
        try:
            # TODO: this url is project specific. Either it has to be a config option or some other way has to be found
            self.client.workspace.get_status(
                path="/Workspace/Repos/nippon/nippon_production_scheduling/requirements.txt"
            )
            return True
        except Exception as err:
            logger.error(f"Error: {err}")
            return False

    def get_orch_info(self, orch_name, method="GET"):
        """
        Get information about a job in Databricks
        https://docs.databricks.com/api/workspace/jobs/get
        """
        # TODO AGA: decidir si incluir las url de documentacion en el código
        url = f"{self.url}/api/2.1/jobs/get/?job_id={orch_name}"
        schema_info = self.request_headers_auth(method=method, url=url)
        if "error_code" in schema_info.json().keys():
            raise DatabricksError("JOB not available")
        return schema_info

    # TODO AGA: incluir un id de job por defecto o hacer obligatorio el uso el parámetro.
    #   Revisar los efectos secundarios de eliminar execution_id y usar el predeterminado
    def run_workflow(
        self,
        execution_id,
        orch_name=config_orchestrator["databricks"]["def_schema"],
        checks_only=False,
        case_id=None,
    ):
        """
        Run a job in Databricks
        """
        # TODO AGA: revisar si la url esta bien/si acepta asi los parámetros
        url = f"{self.url}/api/2.1/jobs/run-now/"
        # TODO AGA: revisar si deben ser notebook parameters o job parameters.
        #   Entender cómo se usa checks_only
        payload = dict(
            job_id=orch_name, notebook_parameters=dict(checks_only=checks_only)
        )
        return self.request_headers_auth(method="POST", url=url, json=payload)

    def get_run_status(self, workflow_name, run_id):
        """
        Get the status of a run in Databricks
        """
        url = f"{self.url}/api/2.1/jobs/runs/get"
        payload = dict(run_id=run_id)
        info = self.request_headers_auth(method="POST", url=url, json=payload)
        info = info.json()
        state = info["status"]
        return state

    def request_headers_auth(self, status=200, **kwargs):
        def_headers = {"Authorization": "Bearer " + str(self.token)}
        headers = kwargs.get("headers", def_headers)
        response = requests.request(headers=headers, **kwargs)
        if status is None:
            return response
        if response.status_code != status:
            raise DatabricksError(error=response.text, status_code=response.status_code)
        return response
