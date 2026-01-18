from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField()
    def _str_(self):
        return self.name

class Book(models.Model):
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        related_name="books"
    )

class Library(models.Model):
    name = models.CharField()
    books = models.ManyToManyField(Book, related_name= "Library")

class Librarian(models.Model):
    name = models.CharField()
    library = models.OneToOneField(Library, on_delete= models.CASCADE)