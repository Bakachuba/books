from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BookSerializer


class BooksApiTestCase(APITestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(name="Test book 1", price=25,
                                          author_name='Author 1')
        self.book_2 = Book.objects.create(name="Test book 2", price=55,
                                          author_name='Author 2')
        self.book_3 = Book.objects.create(name="Test book 3 Author 1", price=65,
                                          author_name='Author 3')
    def test_get(self):
        url = reverse('book-list')
        # print(url)
        response = self.client.get(url)
        serializer_data = BookSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # self.assertEqual(status.HTTP_202_ACCEPTED, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('book-list')
        # print(url)
        response = self.client.get(url, {'filter': 'price'})
        serializer_data = BookSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # self.assertEqual(status.HTTP_202_ACCEPTED, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('book-list')
        # print(url)
        response = self.client.get(url, data={'search': 'Author 1'})
        serializer_data = BookSerializer([self.book_1, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # self.assertEqual(status.HTTP_202_ACCEPTED, response.status_code)
        self.assertEqual(serializer_data, response.data)
    # print(response.data)

    def test_get_sort(self):
        expected_order = [self.book_1, self.book_3, self.book_2]
        # Serialize the expected order
        serializer_data = BookSerializer(expected_order, many=True).data
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'price'})
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # Check if the expected data is a subset of the response data
        self.assertCountEqual(serializer_data, response.data)

    def test_get_sort_author(self):
        expected_order = [self.book_1, self.book_3, self.book_2]
        # Serialize the expected order
        serializer_data = BookSerializer(expected_order, many=True).data
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'author_name'})
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # Check if the expected data is a subset of the response data
        self.assertCountEqual(serializer_data, response.data)