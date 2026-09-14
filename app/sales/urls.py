from django.urls import path

from .views import SaleCreateView, SaleListView, SaleUpdateView, SaleDeleteView


urlpatterns = [
    path('sales/create/', SaleCreateView.as_view(), name='sale-create'),
    path('sales/list/', SaleListView.as_view(), name='sale-list'),
    path('sales/<int:pk>/', SaleUpdateView.as_view(), name='sale-update'),
    path('sales/<int:pk>/delete/', SaleDeleteView.as_view(), name='sale-delete'),
]