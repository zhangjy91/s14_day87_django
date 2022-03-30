from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from app03.models import UserToken

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
