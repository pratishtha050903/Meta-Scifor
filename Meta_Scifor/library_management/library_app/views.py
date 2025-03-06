from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import Book, Borrow
from .forms import BookForm, BorrowForm
from django.utils.timezone import now
from datetime import timedelta




from django.contrib.auth import get_user_model

User = get_user_model()



def home(request):
    return render(request, "home.html")

from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'library_app/book_list.html', {'books': books})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book
from .forms import BookForm

def is_librarian(user):
    return user.is_authenticated and user.is_staff  # Librarians only

@login_required
@user_passes_test(is_librarian)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after adding
    else:
        form = BookForm()

    return render(request, 'library_app/book_form.html', {'form': form})

@login_required
@user_passes_test(is_librarian)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after editing
    else:
        form = BookForm(instance=book)

    return render(request, 'library_app/book_form.html', {'form': form, 'book': book})

@login_required
@user_passes_test(is_librarian)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":  # Confirm delete
        book.delete()
        return redirect('book_list')

    return render(request, 'library_app/book_delete.html', {'book': book})




@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.quantity < 1:
        return redirect('book_list')  # Prevent borrowing if out of stock

    if request.method == "POST":
        form = BorrowForm(request.POST)
        if form.is_valid():
            borrow = form.save(commit=False)
            borrow.user = request.user
            borrow.book = book
            borrow.due_date = now().date() + timedelta(days=7)  # Set due date
            book.quantity -= 1  # Decrease quantity
            book.save()
            borrow.save()
            return redirect('borrowed_books')

    else:
        form = BorrowForm()

    due_date = now().date() + timedelta(days=7)
    return render(request, 'library_app/borrow_book.html', {'form': form, 'book': book, 'due_date': due_date})



@login_required
def borrowed_books(request):
    today = now().date()
    fine_per_day = 10  # Adjust fine amount

    # Fetch only books borrowed by the logged-in user
    borrowed_books = Borrow.objects.filter(user=request.user)

    for borrow in borrowed_books:
        if not borrow.returned:  # If book is not returned
            due_date = borrow.borrow_date + timedelta(days=7)  # 7-day limit
            if today > due_date:  # If overdue
                overdue_days = (today - due_date).days
                borrow.fine = overdue_days * fine_per_day
                borrow.save()  # Save updated fine in DB

    return render(request, 'library_app/borrowed_books.html', {'borrowed_books': borrowed_books})

@login_required
@user_passes_test(lambda u: u.is_staff)  # Only librarians can do this
def increase_quantity(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.quantity += 1  # Increase book quantity
    book.save()
    return redirect('book_list')
