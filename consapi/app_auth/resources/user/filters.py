from django_filters.filters import OrderingFilter
from django_filters import rest_framework as filters
from django.contrib.auth.models import User


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(
        field_name='username',
        lookup_expr='icontains_accinsensitive'
        )

    order_by_field = 'username'

    ordering = OrderingFilter(
        fields=(
            ('username', 'username'),
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            )
