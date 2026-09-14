from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .models import Sale
from .serializers import SaleCreateSerializer, SaleSerializer, SaleUpdateSerializer
from company.permissions import IsCompanyMember

@extend_schema(tags=['sales'])
class SaleCreateView(CreateAPIView):
    serializer_class = SaleCreateSerializer
    permission_classes = [IsCompanyMember]

@extend_schema(tags=['sales'])
class SaleListView(ListAPIView):
    serializer_class = SaleSerializer
    permission_classes = [IsCompanyMember]

    def get_queryset(self):
        return Sale.objects.filter(company=self.request.user.company)

@extend_schema(tags=['sales'])
class SaleUpdateView(UpdateAPIView):
    serializer_class = SaleUpdateSerializer
    permission_classes = [IsCompanyMember]

    http_method_names = ["patch"]

    def get_queryset(self):
        return Sale.objects.filter(company=self.request.user.company)

@extend_schema(tags=['sales'])
class SaleDeleteView(DestroyAPIView):
    serializer_class = SaleSerializer
    permission_classes = [IsCompanyMember]

    def get_queryset(self):
        return Sale.objects.filter(company=self.request.user.company)