"""

"""

from cornflow_core.models import TraceAttributesModel
from cornflow_core.shared import database


class RoleBaseModel(TraceAttributesModel):
    __abstract__ = True
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(128), nullable=False)

    def __init__(self, data):
        super().__init__()
        self.id = data.get("id")
        self.name = data.get("name")

    def __repr__(self):
        return f"<Role {self.name}>"

    def __str__(self):
        return self.__repr__()
