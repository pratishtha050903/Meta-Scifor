from django.db import models
from users.models import CustomUser
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth import get_user_model
def default_due_date():
    return now() + timedelta(days=14)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)  # New field

    @property
    def available(self):
        return self.quantity > 0  # Book is available if quantity > 0

    def __str__(self):
        return f"{self.title} ({self.quantity} available)"

class Borrow(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(default=now)  # When the book was borrowed
    due_date = models.DateField(blank=True, null=True)  # When the book should be returned
    returned = models.BooleanField(default=False)  # Track if the book is returned ✅
    fine = models.IntegerField(default=0)  # Fine amount if overdue

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = self.borrow_date + timedelta(days=7)  # Set default due date
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"