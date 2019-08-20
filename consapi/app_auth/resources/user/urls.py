from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet

# r = routers.DefaultRouter()

# r.register(r'user', UserViewSet.as_view(),
# 	base_name='user')

urlpatterns =  [
	# url(r'', include(r.urls))
	url('users', UserViewSet.as_view(), name='users')
]