from rest_framework.permissions import BasePermission


class IsStorageCompanyMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated
            and request.user.company_id == obj.company_id
        )

class IsStorageOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated
            and request.user.is_company_owner
            and request.user.company_id == obj.company_id
        )