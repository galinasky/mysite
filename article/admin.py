from django.contrib import admin
from article.models import Article,Comments
# Register your models here.
class ArticleInline(admin.StackedInline):
    model=Comments
    extra=2

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['Article_title','Article_date']
    fields=['Article_title','Article_text','Article_date']
    search_fields = ['Article_title']
    inlines=[ArticleInline]
    list_filter=['Article_date']


admin.site.register(Article,ArticleAdmin)
