from django.contrib import admin
from .models import Post, Category, Tag, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'rate', 'created_at']
    list_display_links = ['title']
    search_fields = ['title']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)