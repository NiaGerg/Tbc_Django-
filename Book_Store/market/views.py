from IPython.core.page import page
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from market.models import Book


def get_books(request):
    books = Book.objects.all().order_by('name')
    return_books = []
    for book in books:
        return_books.append({
            'name': book.name,
            'page_count': book.page_count,
            'category': book.category,
            'author_name': book.author_name,
            'price': str(book.price),
            'image_url': book.image.url if book.image else None,
        })
    return JsonResponse(return_books, safe=False)


def get_book(request, book_id):
    book = Book.objects.all().get(pk=book_id)
    return render(request, 'market/books/details.html', {'book': book})


def index(request):
    page_size = 3
    name = request.GET.get('name', '')
    page_number = request.GET.get('page', 1)
    books_list = Book.objects.filter(name__icontains=name)

    paginator = Paginator(books_list, page_size)
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'books': books})
