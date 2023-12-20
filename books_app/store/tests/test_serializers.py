from unittest import TestCase

from django.contrib.auth.models import User

from store.models import Book
from store.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create(username="user1", password="password")
        self.user_2 = User.objects.create(username="user2", password="password")

    def test_ok(self):
        book_1 = Book.objects.create(name="Test book 1", price=25,
                                     author_name="Author 1",
                                     owner=self.user_1)
        book_2 = Book.objects.create(name="Test book 2", price=55,
                                     author_name="Author 2",
                                     owner=self.user_2)
        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price': '25.00',
                'author_name': 'Author 1',
                'owner': book_1.owner.id
            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '55.00',
                'author_name': 'Author 2',
                'owner': book_2.owner.id
            },
        ]
        # print("Expected data:", expected_data)
        # print("Actual data:", data)
        # print("User 1 ID:", self.user_1.id)
        # print("User 2 ID:", self.user_2.id)

        self.assertEqual(expected_data, data)