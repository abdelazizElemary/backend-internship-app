from django.contrib import admin

from books.models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','category','publish_date','created')
admin.site.register(Book, BookAdmin)