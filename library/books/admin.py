from django.contrib import admin

from books.models import MyUser, Book


# Register your models here.
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'quantity')
    list_filter = ("author", )



admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Book, BookAdmin)
