from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .models import Storage
from company.permissions import IsCompanyOwner
from .permissions import IsStorageCompanyMember, IsStorageOwner
from .serializers import StorageSerializer

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
    permission_classes = [IsStorageCompanyMember]

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