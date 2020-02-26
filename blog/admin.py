from django.contrib import admin
from .models import Post

# create columns for PostAdmin page
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')

admin.site.register(Post, PostAdmin)
