"""URL configuration for the littlelemon project."""
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    # Djoser endpoints for user registration & token-based auth
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # Convenience: legacy DRF token endpoint
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
