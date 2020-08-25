from django.contrib import admin

from .models import Article, Variant

class RelationshipInline(admin.TabularInline):
    model = Variant

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

