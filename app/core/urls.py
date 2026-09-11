from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from users.auth_views import LoginView, RefreshTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("api/v1/users/", include("users.urls")),
    path("api/v1/companies/", include("company.urls")),
    path('api/v1/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('api/v1/', include("storage.urls")),
    path('api/v1/', include("suppliers.urls")),
]
