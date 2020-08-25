from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Variant

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_theme_count = 0
        for form in self.forms:
            if form.cleaned_data.get('main') is True:
                main_theme_count += 1
        if main_theme_count == 0:
            raise ValidationError('Главный тематический раздел не выбран')
        elif main_theme_count > 1:
            raise ValidationError('Главный тематический раздел может быть только один')
        return super().clean()

class RelationshipInline(admin.TabularInline):
    model = Variant
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

