from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Разрешение, позволяющее производить действия с объектами
    только пользователям с правами администратора.
    """

    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.is_admin)
