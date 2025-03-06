from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now, timedelta


class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=[('librarian', 'Librarian'), ('member', 'Member')], default='member')
    is_librarian = models.BooleanField(default=False)  # Merged from old User model

 # Checkbox for librarian role


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)  # New field for tracking available copies

    def is_available(self):
        return self.quantity > 0  # Check if at least one copy is available

    def __str__(self):
        return f"{self.title} by {self.author} ({self.quantity} available)"


class Borrow(models.Model):
    def seven_days_later():
        return now() + timedelta(days=7)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="borrows")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(default=now)
    due_date = models.DateTimeField(default=seven_days_later)
    returned = models.BooleanField(default=False)
    fine = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def calculate_fine(self):
        if not self.returned and now() > self.due_date:
            overdue_days = (now() - self.due_date).days
            self.fine = overdue_days * 10  # ₹10 per day fine
            self.save()

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
