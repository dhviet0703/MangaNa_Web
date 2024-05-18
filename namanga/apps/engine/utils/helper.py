from namanga.apps.engine.models_container.enum_type import SystemRoleEnum


def check_role_crud_manga(role_user):
    role_access = [SystemRoleEnum.ADMIN.value, SystemRoleEnum.SUPER_ADMIN.value,
                   SystemRoleEnum.POSTER.value]
    return bool(role_user in role_access)
