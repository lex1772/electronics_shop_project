from django.urls import path

from suppliers.apps import SuppliersConfig
from suppliers.views import (
    LinkCreateAPIView,
    LinkListAPIView,
    LinkRetrieveAPIView,
    LinkUpdateAPIView,
    LinkDestroyAPIView)

app_name = SuppliersConfig.name

# урлы для приложения объектов сети
urlpatterns = [
    path('create/', LinkCreateAPIView.as_view(), name='link_create'),
    path('', LinkListAPIView.as_view(), name='link_list'),
    path('<int:pk>/', LinkRetrieveAPIView.as_view(), name='link'),
    path('update/<int:pk>/', LinkUpdateAPIView.as_view(), name='link_update'),
    path('delete/<int:pk>/', LinkDestroyAPIView.as_view(), name='link_delete'),
]
