from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        self.message = (
            'Для доступпа к данной странице необходимо авторизироваться!')

        if request.user.is_authenticated:
            return (request.method in permissions.SAFE_METHODS
                    or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        self.message = 'Изменение чужого контента запрещено!'
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                )
