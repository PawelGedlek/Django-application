from django.contrib import admin
from .models import Category, Movie, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class FilmAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'year', 'film_director', 'trailer', 'after_premiere', 'created_at', 'updated_at']
    list_filter = ['after_premiere', 'created_at', 'updated_at']
    list_editable = ['year', 'film_director', 'after_premiere']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Movie, FilmAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment')

admin.site.register(Comment, CommentAdmin)