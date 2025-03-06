from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()  # ✅ Ensures the correct user model is used

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # ✅ Now uses CustomUser instead of auth.User
        fields = ['username', 'password1', 'password2']


from django.contrib.auth.models import User

class LibrarianRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_staff = True  # Mark librarian as staff
        if commit:
            user.save()
        return user

