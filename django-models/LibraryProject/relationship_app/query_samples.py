from relationship_app.models import Author, Book, Library, Librarian
author = Author.objects.get(name = "Dostoevsky")
books_by_author = Book.objects.filter(author = author)

# List all books in a library
library = Library.objects.get(name = "Main Library")
books_in_library = Library.objects.filter(library = library)

#librarian
librarian = Librarian.objects.get(library = library)