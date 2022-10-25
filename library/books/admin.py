from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author')
    # fields = ['book_name' , 'author', 'category' , 'created']
    readonly_fields = ['created']

admin.site.register(Book , BookAdmin)
