from django.contrib import admin

from books import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2","first_name","last_name","email"),
            },
        ),
    )


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'isbn', 'author', 'date_published']
    list_per_page = 10
    list_filter = ['title']
    search_fields = ['genre']


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_per_page = 5
    list_filter = ['email']

#
# @admin.register(models.Review)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ['name,description,datetime']
#     list_per_page = 4
#     search_fields = ['name']

# admin.site.register(models.Book, BookAdmin)
# admin.site.register(models.Author)
