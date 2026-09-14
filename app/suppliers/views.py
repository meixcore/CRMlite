from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from company.permissions import IsCompanyMember
from .models import Supplier, Supply
from .serializers import SupplierSerializer, SupplyCreateSerializer, SupplySerializer

@extend_schema(tags=['supplier'])
class SupplierCreateView(CreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsCompanyMember]

    def perform_create(self, serializer):
        serializer.save(company_id=self.request.user.company_id)

@extend_schema(tags=['supplier'])
class SupplierListView(ListAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsCompanyMember]

    def get_queryset(self):
        return Supplier.objects.filter(company_id=self.request.user.company_id)

@extend_schema(tags=['supplier'])
class SupplierRetrieveView(RetrieveAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsCompanyMember]

    def get_queryset(self):
        return Supplier.objects.filter(company_id=self.request.user.company_id)

@extend_schema(tags=['supplier'])
class SupplierUpdateView(UpdateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsCompanyMember]

    http_method_names = ["patch"]

    def get_queryset(self):
        return Supplier.objects.filter(company_id=self.request.user.company_id)

@extend_schema(tags=['supplier'])
class SupplierDeleteView(DestroyAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsCompanyMember]

    def get_queryset(self):
        return Supplier.objects.filter(company_id=self.request.user.company_id)

@extend_schema(tags=['supply'])
class SupplyCreateView(CreateAPIView):
    serializer_class = SupplyCreateSerializer
    permission_classes = [IsCompanyMember]

@extend_schema(tags=['supply'])
class SupplyListView(ListAPIView):
    serializer_class = SupplySerializer
    permission_classes = [IsCompanyMember]

    def get_queryset(self):
        return Supply.objects.filter(supplier__company_id=self.request.user.company_id)