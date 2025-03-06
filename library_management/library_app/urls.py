from django.urls import path
from .views import book_list, add_book, edit_book, delete_book, home, borrow_book, borrowed_books, increase_quantity

urlpatterns = [
path('', home, name='home'),
    path('books/', book_list, name='book_list'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
path('books/borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('books/borrowed/', borrowed_books, name='borrowed_books'),
path('books/increase/<int:book_id>/', increase_quantity, name='increase_quantity'),
]

