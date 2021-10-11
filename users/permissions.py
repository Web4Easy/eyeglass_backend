from rest_framework import permissions

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        print(view.action)
        if view.action in ['retrieve','list']:
            return True
        elif view.action in ["update","destroy",'create']:
            return request.user.is_authenticated and request.user.is_admin
        else:
            return False
                                                                                                
    # def has_object_permission(self, request, view, obj):
    #     # Deny actions on objects if the user is not authenticated
    #     if not request.user.is_authenticated():
    #         return False

    #     if view.action == 'retrieve':
    #         return obj == request.user or request.user.is_admin
    #     elif view.action in ['update', 'partial_update']:
    #         return obj == request.user or request.user.is_admin
    #     elif view.action == 'destroy':
    #         return request.user.is_admin
    #     else:
    #         return False