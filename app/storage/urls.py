from django.urls import path

from .views import StorageCreateView, StorageRetrieveView, StorageUpdateView, StorageDeleteView, ProductCreateView, \
    ProductListView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    #Склад
    path("storage/<int:pk>/", StorageRetrieveView.as_view(), name="storage-detail"),
    path("storage/create/", StorageCreateView.as_view(), name="storage-create"),
    path("storage/<int:pk>/update/", StorageUpdateView.as_view(), name="storage-manage"),
    path("storage/<int:pk>/delete/", StorageDeleteView.as_view(), name="storage-delete"),

    #Продукт
    path("product/list/", ProductListView.as_view(), name="product-list"),
    path("product/create/", ProductCreateView.as_view(), name="product-create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product-manage"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
]