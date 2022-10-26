from django.contrib import admin
from .models import Book, User
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
