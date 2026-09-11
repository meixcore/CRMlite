from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.exceptions import ValidationError

from .models import Storage, Product
from company.permissions import IsCompanyOwner, IsCompanyMember
from .permissions import IsStorageOwner
from .serializers import StorageSerializer, ProductSerializer


@extend_schema(tags=["storage"])
class StorageCreateView(CreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = [IsCompanyOwner]

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)

@extend_schema(tags=["storage"])
class StorageRetrieveView(RetrieveAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = [IsCompanyMember]

@extend_schema(tags=["storage"])
class StorageUpdateView(UpdateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = [IsStorageOwner]

    http_method_names = ["patch"]

@extend_schema(tags=["storage"])
class StorageDeleteView(DestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = [IsStorageOwner]

@extend_schema(tags=["product"])
class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsCompanyMember]

    def perform_create(self, serializer):
        storage = serializer.validated_data["storage"]

        if storage.company_id != self.request.user.company_id:
            raise ValidationError({"storage": "Этот склад не принадлежит вашей компании"})
        serializer.save()

@extend_schema(tags=["product"])
class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsCompanyMember]

    def get_queryset(self):
        return Product.objects.filter(storage__company=self.request.user.company)

@extend_schema(tags=["product"])
class ProductUpdateView(UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsCompanyMember]

    http_method_names = ["patch"]

    def get_queryset(self):
        return Product.objects.filter(storage__company=self.request.user.company)

@extend_schema(tags=["product"])
class ProductDeleteView(DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsCompanyMember]

    def get_queryset(self):
        return Product.objects.filter(storage__company=self.request.user.company)