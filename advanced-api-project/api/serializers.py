from rest_framework import serializers
from datetime import datetime
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model data.

    Includes:
    - Custom validation to ensure publication_year
      is not in the future.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom field-level validation.
        Ensures the publication year is not greater
        than the current year.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model data.

    Includes:
    - Author name
    - Nested list of books written by the author

    The books field uses BookSerializer and pulls
    data from the related_name='books' defined
    in the Book model.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
