from django.contrib import admin
from .models import Category,Product
from parler.admin import TranslatableAdmin, TranslatableTabularInline

# Register your models here.

class InlineProduct(TranslatableTabularInline):
    model = Product
    extra = 1

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    inlines = [InlineProduct]
    fields = ('page_title', 'page_description', 'name', 'description', 'category_url', 'image', 'bg_image', 'active',)
    list_display = ('name', 'description', 'category_url', 'active',)
    list_filter = ('active',)
    search_fields = ('translations__name', 'translations__description',)

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    fields = ('category', 'name', 'description', 'image', 'price', 'active')
    list_display = ('category', 'name', 'description', 'price', 'active')
    list_filter = ('category', 'price', 'active',)
    search_fields = ('translations__name', 'price',)
