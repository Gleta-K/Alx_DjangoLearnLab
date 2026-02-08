from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer


class ListView(generics.ListAPIView):
    """
    GET /books/
    Read-only for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/
    Read-only for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class UpdateView(generics.UpdateAPIView):
    """
    PUT /books/update/
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        book_id = self.request.data.get("id")
        if not book_id:
            raise ValidationError({"id": "Book ID is required"})
        return Book.objects.get(id=book_id)


class DeleteView(generics.DestroyAPIView):
    """
    DELETE /books/delete/
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        book_id = self.request.data.get("id")
        if not book_id:
            raise ValidationError({"id": "Book ID is required"})
        return Book.objects.get(id=book_id)
