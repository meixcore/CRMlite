from django.urls import path

from .views import CompanyCreateView, CompanyRetrieveView, CompanyUpdateView, CompanyDeleteView


urlpatterns = [
    path("<int:pk>/", CompanyRetrieveView.as_view(), name="company-detail"),
    path("create/", CompanyCreateView.as_view(), name="company-create"),
    path("update/", CompanyUpdateView.as_view(), name="company-manage"),
    path("delete/", CompanyDeleteView.as_view(), name="company-delete"),
]