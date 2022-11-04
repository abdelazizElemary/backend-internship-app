from django.contrib import admin
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    # fields = ['book_name' , 'author', 'category' , 'created']
    readonly_fields = ['created' , 'modified']

admin.site.register(Book , BookAdmin)
admin.site.register(Category)

