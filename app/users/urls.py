from django.urls import path
from .views import UserRegistrationView, AttachUserToCompanyView

urlpatterns = [
    path('attach-user-to-company/', AttachUserToCompanyView.as_view(), name='add_user_to_company'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]