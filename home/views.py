from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from .models import Section
from category.models import Category
from django.core.mail import send_mail
from django.http.response import HttpResponse
from .forms import ContactFrom
from django.contrib import messages

# Create your views here.
def index(request):

    header_data = Section.objects.active_translations().values("translations__page_title" ,"translations__page_description","bg_image").filter(active=True)[0]
    footer_data = Section.objects.active_translations().values("translations__address", "translations__work_days", "email1", "email2", "phone1", "phone2", "work_from", "work_to").filter(active=True)[0]
    data = Section.objects.get(active=True)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            send_mail(subject=request.POST.get('subject'),
                      message=request.POST.get('message'),
                      from_email=request.POST.get('name') + '<' + request.POST.get('email') + '>',
                      recipient_list=['test@mail.com'])
            messages.success(request,_("Your message has been sent. Thank you!"),extra_tags='success')
            return redirect('home')
        else:
            messages.warning(request, _("Fail to send, check your data!!"), extra_tags='warning')
            return render(request,'index.html',{'header_data':header_data, 'footer_data':footer_data, 'data':data, 'categories': categories, 'form':form},)
    else:
        form = ContactFrom()
        return render(request,'index.html',{'header_data':header_data, 'footer_data':footer_data, 'data':data, 'categories': categories, 'form':form})
