from django.contrib import admin

from books.models import Book


# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'quantity')
    list_filter = ("author", )



admin.site.register(Book, BookAdmin)
