from django.contrib import admin
from .models import Book, Author

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    title = ['book_name', 'book_category', 'book_author', 'pub_date']
    search_fields = ['book_name']
    list_filter = ['book_author', 'book_category', 'pub_date']
    list_display = ['book_name', 'book_author', 'book_category', 'pub_date']

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['author_name']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
