from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from company.permissions import IsCompanyMember
from .models import Supplier, Supply
from .serializers import SupplierSerializer, SupplyCreateSerializer, SupplySerializer

@extend_schema(tags=['supplier'])
class SupplierCreateView(CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsCompanyMember]

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)

@extend_schema(tags=['supplier'])
class SupplierListView(ListAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsCompanyMember]

    def get_queryset(self):
        return Supplier.objects.filter(company=self.request.user.company_id)

@extend_schema(tags=['supplier'])
class SupplierRetrieveView(RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsCompanyMember]

@extend_schema(tags=['supplier'])
class SupplierUpdateView(UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsCompanyMember]

    http_method_names = ["patch"]

@extend_schema(tags=['supplier'])
class SupplierDeleteView(DestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsCompanyMember]

@extend_schema(tags=['supply'])
class SupplyCreateView(CreateAPIView):
    serializer_class = SupplyCreateSerializer
    permission_classes = [IsCompanyMember]

@extend_schema(tags=['supply'])
class SupplyListView(ListAPIView):
    serializer_class = SupplySerializer
    permission_classes = [IsCompanyMember]

    def get_queryset(self):
        return Supply.objects.filter(supplier__company=self.request.user.company)