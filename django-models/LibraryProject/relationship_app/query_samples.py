from relationship_app.models import Author, Book, Library, Librarian
author_name = "Dostoevsky"
author = Author.objects.get(name =author_name)
books_by_author = Book.objects.filter(author = author)

# List all books in a library
library_name = "Main Library"
library = Library.objects.get(name=library_name)
books = library.books.all()

#librarian
librarian = Librarian.objects.get(library = library)