# from erp.core.security import ModelPermission


class ModulePermission(ModelPermission):
    """
    Se extiende a esta clase de permiso para definir explicitamente éste
    por ser una entidad. Así mismo, sus permisos estan definidos, si en caso
    no es entidad usar BasePermission
    """
    pass
