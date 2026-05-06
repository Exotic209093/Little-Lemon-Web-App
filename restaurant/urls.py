from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'booking/tables', views.BookingViewSet, basename='booking-tables')

urlpatterns = [
    path('', views.index, name='index'),
    path('api/menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('api/menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('api/', include(router.urls)),
]
