"""
Model for the executions
"""

# Import from libraries
import hashlib

# Imports from sqlalchemy
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.dialects.postgresql import TEXT

# Imports from internal modules
from .meta_model import BaseDataModel
from ..shared.const import DEFAULT_EXECUTION_CODE, EXECUTION_STATE_MESSAGE_DICT
from ..shared.utils import db


class ExecutionModel(BaseDataModel):
    """
    Model class for the Executions.
    It inherits from :class:`BaseDataModel` to have the trace fields and user field

    - **id**: str, the primary key for the executions, a hash generated upon creation of the execution
      and the id given back to the user.
      The hash is generated from the creation date, the user and the id of the parent instance.
    - **instance_id**: str, the foreign key for the instance (:class:`InstanceModel`). It links the execution to its
      parent instance.
    - **name**: str, the name of the execution given by the user.
    - **description**: str, the description of the execution given by the user. It is optional.
    - **config**: dict (JSON), the configuration to be used in the execution (:class:`ConfigSchema`).
    - **data**: dict (JSON), the results from the execution (:class:`DataSchema`).
    - **log_text**: text, the log generated by the airflow webserver during execution. This log is stored as text.
    - **log_json**: dict (JSON), the log generated by the airflow webserver during execution.
      This log is stored as a dict (JSON).
    - **user_id**: int, the foreign key for the user (:class:`UserModel`). It links the execution to its owner.
    - **created_at**: datetime, the datetime when the execution was created (in UTC).
      This datetime is generated automatically, the user does not need to provide it.
    - **updated_at**: datetime, the datetime when the execution was last updated (in UTC).
      This datetime is generated automatically, the user does not need to provide it.
    - **deleted_at**: datetime, the datetime when the execution was deleted (in UTC). Even though it is deleted,
      actually, it is not deleted from the database, in order to have a command that cleans up deleted data
      after a certain time of its deletion.
      This datetime is generated automatically, the user does not need to provide it.
    - **state**: int, value representing state of the execution (finished, in progress, error, etc.)
    - **state_message**: str, a string value of state with human readable status message.
    - **data_hash**: a hash of the data json using SHA256

    :param dict data: the parsed json got from an endpoint that contains all the required information to
      create a new execution
    """

    # Table name in the database
    __tablename__ = "executions"

    # Model fields
    id = db.Column(db.String(256), nullable=False, primary_key=True)
    instance_id = db.Column(
        db.String(256), db.ForeignKey("instances.id"), nullable=False
    )
    config = db.Column(JSON, nullable=False)
    dag_run_id = db.Column(db.String(256), nullable=True)
    log_text = db.Column(TEXT, nullable=True)
    log_json = db.Column(JSON, nullable=True)
    state = db.Column(db.SmallInteger, default=DEFAULT_EXECUTION_CODE, nullable=False)
    state_message = db.Column(
        TEXT,
        default=EXECUTION_STATE_MESSAGE_DICT[DEFAULT_EXECUTION_CODE],
        nullable=True,
    )

    def __init__(self, data):
        super().__init__(data)
        self.user_id = data.get("user_id")
        self.instance_id = data.get("instance_id")
        self.id = hashlib.sha1(
            (
                str(self.created_at)
                + " "
                + str(self.user_id)
                + " "
                + str(self.instance_id)
            ).encode()
        ).hexdigest()

        self.dag_run_id = data.get("dag_run_id")
        self.state = data.get("state", DEFAULT_EXECUTION_CODE)
        self.state_message = EXECUTION_STATE_MESSAGE_DICT[self.state]
        self.config = data.get("config")
        self.log_text = data.get("log_text")
        self.log_json = data.get("log_json")

    def update_state(self, code, message: None):
        """
        Method to update the state code and message of an execution

        :param int code: State code for the execution
        :param str message: Message for the error
        :return: nothing
        """
        self.state = code
        if message is None:
            self.state_message = EXECUTION_STATE_MESSAGE_DICT[code]
        else:
            self.state_message = message
        super().update({})

    def __repr__(self):
        """
        Method to represent the class :class:`ExecutionModel`

        :return: The representation of the :class:`ExecutionModel`
        :rtype: str
        """
        return "<id {}>".format(self.id)

    def __str__(self):
        """
        Method to print a string representation of the :class:`ExecutionModel`

        :return: The string for the :class:`ExecutionModel`
        :rtype: str
        """
        return "<id {}>".format(self.id)
