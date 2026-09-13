from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from company.permissions import IsCompanyOwner

from .serializers import RegisterSerializer, AttachUserSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["users"])
class UserRegistrationView(CreateAPIView):
    permission_classes=[]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class AttachUserToCompanyView(APIView):
    permission_classes = [IsCompanyOwner]

    @extend_schema(
        request=AttachUserSerializer,
        tags=["users"],
    )
    def post(self, request):
        serializer = AttachUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]

        user = User.objects.get(email=email)
        if user.is_company_owner:
            return Response({"detail": "Владелец компании не может быть добавлен в другую компанию"}, status=403)

        if user.company is not None:
            return Response({"detail": "Пользователь уже связан с компанией"}, status=403)

        user.company = request.user.company
        user.is_company_owner = False
        user.save()

        return Response({"detail": "Пользователь добавлен в компанию"})