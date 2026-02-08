from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/update/
    PATCH /books/update/

    Expects book ID in request body.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        book_id = self.request.data.get('id')
        if not book_id:
            raise ValidationError({"id": "Book ID is required for update."})
        return Book.objects.get(id=book_id)


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/delete/

    Expects book ID in request body.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        book_id = self.request.data.get('id')
        if not book_id:
            raise ValidationError({"id": "Book ID is required for deletion."})
        return Book.objects.get(id=book_id)
