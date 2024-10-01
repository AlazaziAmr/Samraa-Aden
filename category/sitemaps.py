from django.contrib.sitemaps import Sitemap
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Category

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()