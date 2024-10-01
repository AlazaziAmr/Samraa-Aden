from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.utils.translation import gettext_lazy as _


class ContactFrom(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _("Name"), 'class': 'form-control'}),max_length=50,required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': _("Email"), 'class': 'form-control'}),required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _("Subject"), 'class': 'form-control'}),max_length=200,required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _("Message"), 'class': 'form-control', 'rows':5}),max_length=2000,required=True)
    captcha = ReCaptchaField(
        public_key='6Lez1FkpAAAAACX97KEvC7PKlPkz7V-szEW9l6X9',
        private_key='6Lez1FkpAAAAAF-FHJIVzZUNbCFAFtrZr5QGnKb0',
        widget=ReCaptchaV2Checkbox(attrs={'data-callback':'enableBtn'}),
        required = True
    )

    # def __init__(self, *args, **kwargs):
    #     super(ContactFrom, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'