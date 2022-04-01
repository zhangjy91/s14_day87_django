from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import BasePermission

from app03.models import UserToken,User

class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get('token')
        if token:
            user_token = UserToken.objects.filter(token=token).first()
            if user_token:
                return user_token.user,token
            else:
                raise AuthenticationFailed('认证失败')
        else:
            raise AuthenticationFailed('请求中需要携带token')

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        print(user.get_user_type_display())

        if user.user_type == 1:
            return True
        else:
            return False
