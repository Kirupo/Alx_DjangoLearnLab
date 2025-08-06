from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        self.author = Author.objects.create(name="Author One")

        self.book_data = {
            'title': 'Test Book',
            'author_id': self.author.id,
            'published_date': '2025-01-01'
        }

        self.book = Book.objects.create(title="Existing Book", author=self.author, published_date='2025-02-02')

    def test_create_book(self):
        url = reverse('book-list')
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        updated_data = {
            'title': 'Updated Book',
            'author_id': self.author.id,
            'published_date': '2025-02-02'
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books_by_author(self):
        url = reverse('book-list') + f'?author={self.author.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Existing'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_books_by_title(self):
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_access(self):
        self.client.logout()
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class AuthorListViewTest(APITestCase):
    def setUp(self):
        Author.objects.create(name="Test Author")

    def test_author_list_status_code_and_data(self):
        url = reverse('author-list')  # Make sure your url name is correct
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Author', str(response.data))  # This checks response.data content

class BookListViewTest(APITestCase):
    def setUp(self):
        author = Author.objects.create(name="Book Author")
        Book.objects.create(title="Test Book", author=author, publication_year=2020)

    def test_book_list_status_code_and_data(self):
        url = reverse('book-list')  # Make sure your url name is correct
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', str(response.data))  # Checks response.data content
