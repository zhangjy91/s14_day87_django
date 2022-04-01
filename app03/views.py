from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from app03.models import Fruit
from app03.ser import FruitSerializers
from app03.app_auth import MyAuthentication

from app03.app_auth import MyPermission, MyAuthentication

class FruitView(APIView):
    # authentication_classes = [MyAuthentication]
    # permission_classes = [MyPermission]
    def get(self,request):
        fruit = Fruit.objects.all()
        print('33333333' + request.user.username)
        1/0
        fruit_ser = FruitSerializers(fruit, many=True)
        return Response(fruit_ser.data)

    def post(self,request):
        fruit_ser = FruitSerializers(data=request.data)
        if fruit_ser.is_valid():
            fruit_ser.save()
            return Response(fruit_ser.data)
        else:
            return Response({"status":101, "msg":"新增失败"})

class FruitDetailView(APIView):
    def get(self,request,pk):
        fruit = Fruit.objects.filter(id=pk).first()
        fruit_ser = FruitSerializers(fruit)
        return Response(fruit_ser.data)

    def put(self,request,pk):
        fruit = Fruit.objects.filter(id=pk).first()
        fruit_ser = FruitSerializers(instance=fruit,data=request.data)
        if fruit_ser.is_valid():
            fruit_ser.save()
            return Response(fruit_ser.data)
        else:
            return Response({'status':101,'msg':'修改失败'})

    def delete(self,request,pk):
        Fruit.objects.filter(id=pk).delete()
        return Response({'status':100, 'msg':'删除成功'})


from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.throttling import AnonRateThrottle

class Fruit2View(ListCreateAPIView):
    throttle_classes = [AnonRateThrottle]
    queryset = Fruit.objects
    serializer_class = FruitSerializers

class Fruit2DetailView(RetrieveUpdateDestroyAPIView):
    queryset = Fruit.objects
    serializer_class = FruitSerializers

from rest_framework.viewsets import ModelViewSet

from app03.app_auth import MyAuthentication,MyPermission


class Fruit3View(ModelViewSet):
    authentication_classes = [MyAuthentication]
    permission_classes = [MyPermission]
    queryset = Fruit.objects
    serializer_class = FruitSerializers

from rest_framework.viewsets import ModelViewSet

from app03.models import Fruit
from app03.ser import FruitSerializers

class Fruit4ViewSet(ModelViewSet):
    queryset = Fruit.objects
    serializer_class = FruitSerializers

from app03.models import User,UserToken
import uuid

class LoginView(APIView):
    # authentication_classes = [MyAuthentication]
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        print('username: ' + username)
        print('password ' + password)

        user = User.objects.filter(username=username, password=password).first()
        # print('22222' + user.username)
        if user:
            token = uuid.uuid4()
            UserToken.objects.update_or_create(defaults={'token':token}, user=user)
            return Response({'status':100, 'msg':'登录成功', 'token':token})
        else:
            return Response({'status':101, 'msg':'用户名或密码错误'})


from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

from app03.models import Fruit
from app03.ser import FruitSerializers

class Fruit5View(ListAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializers

    filter_fields = ('name','price',)

    filter_backends = [OrderingFilter]
    ordering_fields = ('id','price',)


from app03.app_auth import APIResponse

class Fruit6View(APIView):
    def get(self,request):
        return APIResponse(data={'name':'zhangqi','age':22,},token='2342sdff',ss='ssssssss')
        # return APIResponse()