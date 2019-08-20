from django.contrib.auth.models import User


class QuerySet(object):
    """
    Consulta orm de la entidad si en caso contiene mas lógica extender a un directorio
    managers para descomponer las funciones que son utilizadas para un mejor entendimiento
    del requerimiento.
    """

    relateds = (
    )

    onlys = (
        'id',
        'name'
    )

    annotates = dict(
    )

    def get_queryset(self):
        q = User.objects.select_related(
            *self.relateds).annotate(
            **self.annotates).all()
        return q
