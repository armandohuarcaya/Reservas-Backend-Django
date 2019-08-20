from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics, permissions
from .queryset import QuerySet
from .serializers import UserSerializer
from .filters import UserFilter
#from .permissions import UserPermission

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class UserViewSet(QuerySet, generics.ListCreateAPIView):
	renderer_classes = (JSONRenderer,)
	permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	filter_class = UserFilter
	serializer_class = UserSerializer
	