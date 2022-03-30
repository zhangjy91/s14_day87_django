from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from app02.models import Book
from app02.ser import BookSerializer


class Book2View(APIView):

    def get(self,request,pk):
        response_msg = {'status': 100, 'msg': '查询成功'}
        book = Book.objects.filter(id=pk).first()
        print(book)
        book_ser = BookSerializer(book)
        response_msg['data'] = book_ser.data
        return Response(response_msg, status=status.HTTP_405_METHOD_NOT_ALLOWED, headers={'token':'345sflkeoi'})