from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import Book
# from app01.ser import BookModelSerializer
#
# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer


from rest_framework.views import APIView
from app01.models import Book
from app01.ser import BookSerializer,BookModelSerializer
from rest_framework.response import Response
from django.http import JsonResponse

class BookView(APIView):

    def get(self,request,pk):
        response_msg = {'status': 100, 'msg': '查询成功'}
        book = Book.objects.filter(nid=pk).first()
        print(book)
        book_ser = BookSerializer(book)
        response_msg['data'] = book_ser.data
        return Response(response_msg)
        # return JsonResponse(book_ser.data,json_dumps_params={'ensure_ascii':False})


    def put(self, request, pk):
        response_msg = {'status':100, 'msg':'更新成功'}
        book = Book.objects.filter(nid=pk).first()
        book_ser = BookSerializer(instance=book, data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            response_msg['data'] = book_ser.data
            return Response(response_msg)
        else:
            response_msg['status'] = 101
            response_msg['msg'] = '失败'
            # response_msg['data'] = book_ser.data
            response_msg['error'] = book_ser.errors
            return Response(response_msg)

    def delete(self,request,pk):
        Book.objects.filter(nid=pk).delete()
        return Response({'status':100, 'msg':'删除成功'})


class BooksView(APIView):
    def get(self,request):
        response_msg = {'status': 100, 'msg': '查询成功'}
        books = Book.objects.all()
        books_ser = BookSerializer(books, many=True)
        response_msg['data'] = books_ser.data
        return Response(response_msg)

    def post(self,request):
        response_msg = {'status': 100, 'msg': '新建成功'}
        book_ser = BookSerializer(data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            response_msg['data'] = book_ser.data
        else:
            response_msg['status'] = 101
            response_msg['msg'] = '失败'
            response_msg['error'] = book_ser.errors
        return Response(response_msg)


class BooksView2(APIView):
    def get(self,request):
        response_msg = {'status': 100, 'msg': '查询成功'}
        books = Book.objects.all()
        books_ser = BookModelSerializer(books, many=True)
        response_msg['data'] = books_ser.data
        return Response(response_msg)


class test1():
    pass
