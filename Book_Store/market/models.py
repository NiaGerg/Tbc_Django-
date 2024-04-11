from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name='Title')
    page_count = models.IntegerField(verbose_name='Page Count')
    category = models.CharField(max_length=50, verbose_name='Category')
    author_name = models.CharField(max_length=100, verbose_name='Author')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    image = models.ImageField(upload_to='book_images/', null=True, blank=True, verbose_name='Image')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'