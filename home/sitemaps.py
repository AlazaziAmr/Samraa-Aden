from django.contrib.sitemaps import Sitemap
from .models import Section

class HomeSitemap(Sitemap):
    # i18n = True
    def items(self):
        return Section.objects.filter(active=True)