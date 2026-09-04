from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Company
from .permissions import IsCompanyOwner
from .serializers import CompanySerializer


@extend_schema(tags=["company"])
class CompanyCreateView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.company is not None:
            return Response(
                {
                    "detail": "У пользователя уже есть компания"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        company = serializer.save()

        request.user.company = company
        request.user.is_company_owner = True
        request.user.save(
            update_fields=[
                "company",
                "is_company_owner",
            ]
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(tags=["company"])
class CompanyRetrieveView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["company"])
class CompanyUpdateView(UpdateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsCompanyOwner]

    http_method_names = ["patch"]

    def get_object(self):
        return self.request.user.company

@extend_schema(tags=["company"])
class CompanyDeleteView(DestroyAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsCompanyOwner]

    def get_object(self):
        return self.request.user.company

    def perform_destroy(self, instance):
        user = self.request.user
        instance.delete()
        user.company = None
        user.is_company_owner = False
        user.save(
            update_fields=[
                "company",
                "is_company_owner",
            ]
        )