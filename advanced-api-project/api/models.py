from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Author model represents a writer who can have multiple books.
    This establishes a one-to-many relationship:
    One Author → Many Books
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a published book.

    Each book:
    - Has a title
    - Has a publication year
    - Belongs to exactly one Author (ForeignKey)
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    # ForeignKey creates the one-to-many relationship
    author = models.ForeignKey(
        Author,
        related_name='books',   # Allows author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
