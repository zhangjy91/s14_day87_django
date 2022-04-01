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

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def my_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if not response:
        if isinstance(exc, ZeroDivisionError):
            return Response(data={'status':777, 'msg':'不能除以0 ' + str(exc)},status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'status':999, 'msg':str(exc)},status=status.HTTP_400_BAD_REQUEST)
    else:
        # return response
        return Response(data={'status':888, 'msg':response.data.get('detail')},status=status.HTTP_400_BAD_REQUEST)

    print(exc)
    print(context)


class APIResponse(Response):
    def __init__(self,code=100, msg='成功',data=None,status=None,headers=None,**kwargs):
        dic = {'code':code, 'msg':msg}
        if data:
            dic = {'code':code, 'msg':msg, 'data':data}
        dic.update(kwargs)
        super().__init__(data=dic, status=status,headers=headers)
