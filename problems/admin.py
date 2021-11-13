# problems admin
from django.contrib import admin
from .models import Problem, Comment, ProblemURL

# Register your models here.
class CommentInline(admin.TabularInline):
    model=Comment
    list_display=('comment', 'author', 'created')
    list_filter=('created')
    search_fields=('comment', 'author')

class URLInline(admin.TabularInline):
    model=ProblemURL
    list_display=('url')

class ProblemAdmin(admin.ModelAdmin):
    inlines=[
            CommentInline,
            URLInline,
        ]
    list_display=('title', 'subject', 'topic')

admin.site.register(Problem, ProblemAdmin);