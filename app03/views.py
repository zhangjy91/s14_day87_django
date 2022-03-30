from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from app03.models import Fruit
from app03.ser import FruitSerializers

class FruitView(APIView):

    def get(self,request):
        fruit = Fruit.objects.all()
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

class Fruit2View(ListCreateAPIView):
    queryset = Fruit.objects
    serializer_class = FruitSerializers

class Fruit2DetailView(RetrieveUpdateDestroyAPIView):
    queryset = Fruit.objects
    serializer_class = FruitSerializers

from rest_framework.viewsets import ModelViewSet

class Fruit3View(ModelViewSet):
    queryset = Fruit.objects
    serializer_class = FruitSerializers

from rest_framework.viewsets import ModelViewSet

from app03.models import Fruit
from app03.ser import FruitSerializers

class Fruit4ViewSet(ModelViewSet):
    queryset = Fruit.objects
    serializer_class = FruitSerializers