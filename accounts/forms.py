from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import Users



class UserCreateForm(UserCreationForm):
    class Meta:
        mdoel = Users
        fields = (
            "first_name", "last_name", "phone_number"
        )