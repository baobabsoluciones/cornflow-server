"""
File with the different defined commands
"""
# Import from libraries
from flask_script import Command, Option

# Import from internal modules
from cornflow.models import (
    ActionModel,
    ApiViewModel,
    PermissionViewRoleModel,
    RoleModel,
    UserModel,
    UserRoleModel,
)
from cornflow.shared.const import (
    ADMIN_ROLE,
    ACTIONS_MAP,
    BASE_PERMISSION_ASSIGNATION,
    EXTRA_PERMISSION_ASSIGNATION,
    ROLES_MAP,
    SERVICE_ROLE,
)
from cornflow.endpoints import resources
from cornflow.shared.utils import db


def create_user_with_role(email, password, name, role):
    user = UserModel.get_one_user_by_email(email)
    if user is None:
        data = dict(name=name, email=email, password=password)
        user = UserModel(data=data)
        user.save()
        user_role = UserRoleModel({"user_id": user.id, "role_id": role})
        user_role.save()
        print("{} is created and assigned service role".format(name))
        return True
    user_role = UserRoleModel.get_one_user(user.id)
    if user_role is not None and RoleModel.get_one_object(role) in user_role:
        print("{} exists and already has service role assigned".format(name))
        return True
    user_role = UserRoleModel({"user_id": user.id, "role_id": role})
    user_role.save()
    print("{} already exists and is assigned a service role".format(name))
    return True


class CreateServiceUser(Command):
    """
    Creates the initial super user that is used by airflow to write the results of the execution back
    This command should only be used on deployment
    """

    def get_options(self):
        return (
            Option("-e", "--email", dest="email", help="Service user email"),
            Option("-p", "--password", dest="password", help="Service user password"),
        )

    def run(self, email, password):
        """
        Method to run the command and create the service user

        :param str email: the email for the admin user
        :param str password: the password for the admin user
        :return: a boolean if the execution went right
        :rtype: bool
        """
        return create_user_with_role(email, password, "serviceuser", SERVICE_ROLE)


class CreateAdminUser(Command):
    def get_options(self):
        return (
            Option("-e", "--email", dest="email", help="Admin user email"),
            Option("-p", "--password", dest="password", help="Admin user password"),
        )

    def run(self, email, password):
        """
        Method to run and create the admin user
        :param str email: the email for the admin user
        :param str password: the password for the admin user
        :return: a boolean if the execution went right
        :rtype: bool
        """
        return create_user_with_role(email, password, "admin", ADMIN_ROLE)


class CleanHistoricData(Command):
    """ """

    # TODO: implement command to delete data than is older than X years (this time could be read from a settings file)
    def run(self):
        """

        :return:
        :rtype:
        """
        pass


class RegisterActions(Command):
    def run(self):
        """
        Method to register the actions on the database

        :return: a boolean if the execution went right
        :rtype: bool
        """
        ActionModel.query.delete()
        db.session.commit()

        actions_list = [
            ActionModel(id=key, name=value) for key, value in ACTIONS_MAP.items()
        ]
        db.session.bulk_save_objects(actions_list)
        db.session.commit()

        return True


class RegisterViews(Command):
    def run(self):
        """
        Method to register the endpoints in cornflow

        :return: a boolean if the execution went right
        :rtype: bool
        """
        ApiViewModel.query.delete()
        db.session.commit()

        views_list = [
            ApiViewModel(
                {
                    "name": view["endpoint"],
                    "url_rule": view["urls"],
                    "description": view["resource"].DESCRIPTION,
                }
            )
            for view in resources
        ]
        db.session.bulk_save_objects(views_list)
        db.session.commit()

        return True


class UpdateViews(Command):
    def run(self):
        views_list = [
            ApiViewModel(
                {
                    "name": view["endpoint"],
                    "url_rule": view["urls"],
                    "description": view["resource"].DESCRIPTION,
                }
            )
            for view in resources
            if ApiViewModel.get_one_by_name(view["endpoint"]) is None
        ]
        db.session.bulk_save_objects(views_list)
        db.session.commit()

        return


class RegisterRoles(Command):
    def run(self):
        """
        Method to register the roles in cornflow

        :return: a boolean if the execution went right
        :rtype: bool
        """

        RoleModel.query.delete()
        db.session.commit()

        role_list = [
            RoleModel({"id": key, "name": value}) for key, value in ROLES_MAP.items()
        ]
        db.session.bulk_save_objects(role_list)
        db.session.commit()

        return


class BasePermissionAssignationRegistration(Command):
    def run(self):
        """
        Method to register the base permissions

        :return: a boolean if the execution went right
        :rtype: bool
        """

        PermissionViewRoleModel.query.delete()
        db.session.commit()

        # Create base permissions
        assign_list = [
            PermissionViewRoleModel(
                {
                    "role_id": role,
                    "action_id": action,
                    "api_view_id": ApiViewModel.query.filter_by(name=view["endpoint"])
                    .first()
                    .id,
                }
            )
            for role, action in BASE_PERMISSION_ASSIGNATION
            for view in resources
            if role in view["resource"].ROLES_WITH_ACCESS
        ]

        db.session.bulk_save_objects(assign_list)
        db.session.commit()

        # Create extra permissions
        assign_list = [
            PermissionViewRoleModel(
                {
                    "role_id": role,
                    "action_id": action,
                    "api_view_id": ApiViewModel.query.filter_by(name=endpoint)
                    .first()
                    .id,
                }
            )
            for role, action, endpoint in EXTRA_PERMISSION_ASSIGNATION
        ]

        db.session.bulk_save_objects(assign_list)
        db.session.commit()

        return True


class AccessInitialization(Command):
    def run(self):
        """
        Method to run all access commands together
        :return: a boolean if the execution went right
        :rtype: bool
        """
        RegisterActions().run()
        RegisterViews().run()
        RegisterRoles().run()
        BasePermissionAssignationRegistration().run()
        print("Access initialization ran successfully")
        return True
