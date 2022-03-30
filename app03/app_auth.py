from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        pass
