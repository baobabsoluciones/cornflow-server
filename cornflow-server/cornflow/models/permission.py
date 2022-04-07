from cornflow_core.models import TraceAttributesModel

# from .meta_model import TraceAttributes
from .dag import DeployedDAG
from cornflow_core.shared import database as db


class PermissionViewRoleModel(TraceAttributesModel):
    __tablename__ = "permission_view"
    __table_args__ = (db.UniqueConstraint("action_id", "api_view_id", "role_id"),)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    action_id = db.Column(db.Integer, db.ForeignKey("actions.id"), nullable=False)
    action = db.relationship("ActionModel", viewonly=True)

    api_view_id = db.Column(db.Integer, db.ForeignKey("api_view.id"), nullable=False)
    api_view = db.relationship("ApiViewModel", viewonly=True)

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    role = db.relationship("RoleModel", viewonly=True)

    def __init__(self, data):
        super().__init__()
        self.action_id = data.get("action_id")
        self.api_view_id = data.get("api_view_id")
        self.role_id = data.get("role_id")

    # @classmethod
    # def get_permission(cls, role_id, view_id, action_id):
    #     permission = cls.query.filter_by(
    #         role_id=role_id,
    #         api_view_id=view_id,
    #         action_id=action_id,
    #         deleted_at=None,
    #     ).first()
    #
    #     if permission is not None:
    #         return True

    @classmethod
    def get_permission(cls, **kwargs):
        permission = cls.query.filter_by(deleted_at=None, **kwargs).first()
        if permission is not None:
            return True

    def __repr__(self):
        return f"<Permission role: {self.role_id}, action: {self.action_id}, view: {self.api_view_id}>"


class PermissionsDAG(TraceAttributesModel):
    __tablename__ = "permission_dag"
    __table_args__ = (db.UniqueConstraint("dag_id", "user_id"),)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    dag_id = db.Column(
        db.String(128), db.ForeignKey("deployed_dags.id"), nullable=False
    )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("UserModel", viewonly=True)

    def __init__(self, data):
        super().__init__()
        self.dag_id = data.get("dag_id")
        self.user_id = data.get("user_id")

    def __repr__(self):
        return f"<DAG permission user: {self.user_id}, DAG: {self.dag_id}<"

    @classmethod
    def get_user_dag_permissions(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    @staticmethod
    def add_all_permissions_to_user(user_id):
        dags = DeployedDAG.get_all_objects()
        permissions = [
            PermissionsDAG({"dag_id": dag.id, "user_id": user_id}) for dag in dags
        ]
        for permission in permissions:
            permission.save()

    @staticmethod
    def delete_all_permissions_from_user(user_id):
        permissions = PermissionsDAG.get_user_dag_permissions(user_id)
        for perm in permissions:
            perm.delete()

    @staticmethod
    def check_if_has_permissions(user_id, dag_id):
        permission = PermissionsDAG.query.filter_by(
            user_id=user_id, dag_id=dag_id
        ).first()
        if permission is None:
            return False
        return True
