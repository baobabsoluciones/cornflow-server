from cornflow_core.models import UserRoleBaseModel

# Import from internal modules
from ..shared.const import ADMIN_ROLE, SERVICE_ROLE
from cornflow_core.shared import db


class UserRoleModel(UserRoleBaseModel):
    # TODO: Should have a user_id to store the user that defined the assignation?
    __tablename__ = "user_role"
    __table_args__ = (db.UniqueConstraint("user_id", "role_id"),)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("UserModel", viewonly=True)

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    role = db.relationship("RoleModel", viewonly=True)

    def __init__(self, data):
        """
        Method to initialize th assignation of a role to a user that

        :param dict data: dict with the information needed to  create a new assignation of a role to a user
        """
        super().__init__()
        self.user_id = data.get("user_id")
        self.role_id = data.get("role_id")

    @classmethod
    def is_admin(cls, user_id):
        """
        Method that checks if a given user has the admin role assigned

        :param int user_id: the ID of the user
        :return: a boolean indicating if the user has the admin role assigned or not
        :rtype: boolean
        """
        user_roles = cls.get_all_objects(user_id=user_id)
        for role in user_roles:
            if role.role_id == ADMIN_ROLE:
                return True

        return False

    @classmethod
    def is_service_user(cls, user_id):
        """
        Method that checks if a given user has the service role assigned

        :param int user_id: the ID of the user
        :return: a boolean indicating if the user has the service role assigned or not
        :rtype: boolean
        """
        user_roles = cls.get_all_objects(user_id=user_id)
        for role in user_roles:
            if role.role_id == SERVICE_ROLE:
                return True

        return False

    @classmethod
    def check_if_role_assigned(cls, user_id, role_id):
        """
        Method to check if a user has a given role assigned

        :param int user_id: id of the specific user
        :param int role_id: id of the specific role
        :return: a boolean if the user has the role assigned
        :rtype: bool
        """
        return cls.get_one_object(user_id=user_id, role_id=role_id) is not None

    @classmethod
    def check_if_role_assigned_disabled(cls, user_id, role_id):
        """
        Method to check if a user has a given role assigned but disabled

        :param user_id: id of the specific user
        :param role_id: id of the specific role
        :return: a boolean if the user has the role assigned but disabled
        :rtype: bool
        """
        user_role = cls.query.filter(
            cls.user_id == user_id, cls.role_id == role_id, cls.deleted_at != None
        ).first()
        return user_role is not None

    def __repr__(self):
        """
        Method for the representation of the assigned roles

        :return: the representation
        :rtype: str
        """
        try:
            return f"{self.user.username} has role {self.role.name}"
        except AttributeError:
            return f"{self.user_id} has role {self.role_id}"

    def __str__(self):
        """
        Method for the string representation of the assigned roles

        :return: the string representation
        :rtype: str
        """
        return self.__repr__()
