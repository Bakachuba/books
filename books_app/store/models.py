from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=255)

    def __str__(self):
        # "отображение айди и имен на сайте /admin у книг"
        return f'id: {self.id}; name: {self.name}'
