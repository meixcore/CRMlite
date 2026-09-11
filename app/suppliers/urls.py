from django.urls import path

from .views import SupplierCreateView, SupplierRetrieveView, SupplierListView, SupplierUpdateView, SupplierDeleteView, \
    SupplyCreateView, SupplyListView

urlpatterns = [
    # Поставщик
    path("suppliers/", SupplierListView.as_view(), name="supplier-list"),
    path("suppliers/create/", SupplierCreateView.as_view(), name="supplier-create"),
    path("suppliers/<int:pk>/", SupplierRetrieveView.as_view(), name="supplier-detail"),
    path("suppliers/<int:pk>/update/", SupplierUpdateView.as_view(), name="supplier-update"),
    path("suppliers/<int:pk>/delete/", SupplierDeleteView.as_view(), name="supplier-delete"),

    # Поставка
    path("supplies/create/", SupplyCreateView.as_view(), name="supply-create"),
    path("supplies/list/", SupplyListView.as_view(), name="supply-list"),
]