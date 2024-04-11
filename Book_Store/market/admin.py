from django.contrib import admin
from market.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'price')
    search_fields = ('name', 'author_name')
    list_filter = ('price',)
