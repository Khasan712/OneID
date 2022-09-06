from django.contrib import admin

# Register your models here.
from .models import Users



@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'last_name', 'first_name')
