from django.urls import include, path

urlpatterns = [
    path('user/', include(
        'app_auth.resources.user.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]