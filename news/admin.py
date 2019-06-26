from django.contrib import admin
from .models import Category, Keyword, KeyNews, RankNews, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
admin.site.register(Category, CategoryAdmin)

class KeywordAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category',]
admin.site.register(Keyword, KeywordAdmin)

class KeyNewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url', 'keyword', 'date',]
admin.site.register(KeyNews, KeyNewsAdmin)

class RankNewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url', 'category', 'date',]
admin.site.register(RankNews, RankNewsAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'user', 'keyword',]
admin.site.register(Comment, CommentAdmin)