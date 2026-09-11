from rest_framework.permissions import BasePermission


class IsCompanyOwner(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_company_owner
            and request.user.company is not None
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated
            and request.user.is_company_owner
            and request.user.company_id == obj.id
        )

class IsCompanyMember(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.company_id is not None
        )

    def has_object_permission(self, request, view, obj):
        return request.user.company_id == obj.company_id