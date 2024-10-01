from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from .models import Category
from home.models import Section
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from home.forms import ContactFrom


# Create your views here.
def cat(request, category_url):
    category_data = get_object_or_404(Category, translations__category_url=category_url)
    header_data = Category.objects.active_translations().values("translations__page_title",
                                                                "translations__page_description",
                                                                "bg_image").filter(active=True)[0]
    footer_data = Section.objects.active_translations().values("translations__address", "translations__work_days",
                                                               "email1", "email2", "phone1", "phone2", "work_from",
                                                               "work_to").filter(active=True)[0]
    categories = Category.objects.all()
    queryset = category_data.product_set.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    # categories = Category.objects.values('translations__name','translations__category_url')
    return render(request, 'category.html',
                  {'header_data': header_data,'footer_data': footer_data, 'categories': categories, 'category_data': category_data, 'products': products,
                   'form':ContactFrom})
