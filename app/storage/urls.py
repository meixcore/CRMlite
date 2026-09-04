from django.urls import path

from .views import StorageCreateView, StorageRetrieveView, StorageUpdateView, StorageDeleteView


urlpatterns = [
    path("<int:pk>/", StorageRetrieveView.as_view(), name="storage-detail"),
    path("create/", StorageCreateView.as_view(), name="storage-create"),
    path("<int:pk>/update/", StorageUpdateView.as_view(), name="storage-manage"),
    path("<int:pk>/delete/", StorageDeleteView.as_view(), name="storage-delete"),
]