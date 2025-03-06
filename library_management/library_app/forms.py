from django import forms
from .models import Book, Borrow

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'quantity']

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = []  # No need to show fields since we auto-assign user & book
