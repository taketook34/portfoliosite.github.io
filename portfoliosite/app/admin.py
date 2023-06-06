from django.contrib import admin
from .models import Post, Question

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'screen', 'creation_time')
    search_fields = ('title', 'creation_time')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'contact', 'content')
    search_fields = ('id', 'contact')

admin.site.register(Post, PostAdmin)
admin.site.register(Question, QuestionAdmin)

# Register your models here.
