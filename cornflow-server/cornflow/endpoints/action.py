"""

"""
# Import from libraries
from flask_apispec import marshal_with, doc
from flask_apispec.views import MethodResource

# Import from internal modules
from .meta_resource import MetaResource
from ..models import ActionModel
from ..schemas.action import ActionsResponse
from ..shared.authentication import AuthCornflow
from ..shared.const import ADMIN_ROLE
from cornflow_core.resources import BaseMetaResource


class ActionListEndpoint(BaseMetaResource, MethodResource):
    ROLES_WITH_ACCESS = [ADMIN_ROLE]
    DESCRIPTION = "Endpoint which allows to get the actions defined in the application"
    AUTH_CLASS = AuthCornflow

    def __init__(self):
        super().__init__()
        self.data_model = ActionModel
        # self.query = ActionModel.get_all_objects
        # self.primary_key = "id"

    @doc(description="Get all the actions", tags=["Actions"])
    @marshal_with(ActionsResponse(many=True))
    def get(self):
        """
        API method to get the actions defined in the application.
        It requires authentication to be passed in the form of a token that has to be linked to
        an existing session (login) made by a user.

        :return: A dictionary with the response (data of the actions or an error message)
        and an integer with the HTTP status code.
        :rtype: Tuple(dict, integer)
        """
        return self.get_list()
