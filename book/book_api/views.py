from django.shortcuts import render
from book_api.models import Book
from rest_framework.decorators import api_view
from book_api.serializer import Bookserializer
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = Bookserializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer = Bookserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)    

@api_view(['GET', 'PUT' , 'DELETE'])
def book(request,pk):
    book = Book.objects.get(pk)
    if request.method == 'GET':
        serializer = Bookserializer(book)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = Bookserializer(book, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return serializer.errors

    if request.method == "DELETE":
        book.delete()
        return Response({
            'delete': True
        })
                
