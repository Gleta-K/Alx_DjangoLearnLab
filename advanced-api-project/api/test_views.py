from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):

    def setUp(self):
        """Set up initial data for testing."""
        # Create a user for authentication tests
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(
            title="1984", 
            publication_year=1949, 
            author=self.author
        )
        self.list_url = reverse('book-list')  # Adjust names based on your urls.py
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.id})

    # --- CRUD TESTS ---

    def test_create_book_authenticated(self):
        """Ensure an authenticated user can create a book."""
        self.client.login(username='testuser', password='password123')
        data = {"title": "Animal Farm", "publication_year": 1945, "author": self.author.id}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Verify that a book can be updated."""
        self.client.login(username='testuser', password='password123')
        data = {"title": "1984 - Special Edition", "publication_year": 1949, "author": self.author.id}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "1984 - Special Edition")

    def test_delete_book(self):
        """Ensure a book can be deleted."""
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # --- FILTERING & SEARCHING TESTS ---

    def test_filter_books_by_title(self):
        """Test the filtering functionality."""
        response = self.client.get(f"{self.list_url}?title=1984")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "1984")

    # --- PERMISSIONS TESTS ---

    def test_create_book_unauthenticated(self):
        """Verify that unauthenticated users cannot create books."""
        data = {"title": "Unauthorized Book", "publication_year": 2024, "author": self.author.id}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)