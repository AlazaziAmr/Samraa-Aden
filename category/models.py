from django.db import models
from django.dispatch import receiver
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from django.urls import reverse
from django_resized import ResizedImageField

# Create your models here.

def category_image_path(instance,filename):
    return "images/category/{0}/{1}".format(instance.name,filename)

def product_image_path(Category,filename):
    return "images/category/{0}/{1}".format(Category.name,filename)
class Category(TranslatableModel):
    translations = TranslatedFields(
    page_title = models.CharField(_('page_title'),max_length=60, help_text=_('page_title_help_text')),
    page_description = models.CharField(_('page_description'), help_text=_('page_description_help_text')),
    name = models.CharField(_('category_name'),max_length=100, unique=True, help_text=_('category_name_help_text')),
    description = models.TextField(_('category_description'), help_text=_('category_description_help_text')),
    category_url=models.CharField(_('category_url'), max_length=50, unique=True, help_text=_('category_url_help_text')),
    )
    image = ResizedImageField(_('category_image'), quality=90, force_format="WEBP", upload_to=category_image_path)
    bg_image = ResizedImageField(_('bg_image'), quality=90, force_format="WEBP", upload_to=category_image_path)
    active = models.BooleanField(_('active'), default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cats',args=[self.category_url])

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ['id']

class Product(TranslatableModel):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = ResizedImageField(_('product_image'), quality=90, force_format="WEBP", upload_to=product_image_path)
    translations = TranslatedFields(
    name = models.CharField(_('product_name'),max_length=100, help_text=_('product_name_help_text')),
    description = models.CharField(_('product_description'), help_text=_('product_description_help_text')),
    )
    price = models.PositiveSmallIntegerField(_('price'), default=100, help_text=_('product_price_help_text'),validators=[MinValueValidator(100)])
    active = models.BooleanField(_('active'), default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ['id']

@receiver(models.signals.post_delete, sender=Category)
def delete_Category_image(sender, instance, **kwargs):
    instance.image.delete(save=False)
    instance.bg_image.delete(save=False)

@receiver(models.signals.post_delete, sender=Product)
def delete_Product_image(sender, instance, **kwargs):
    instance.image.delete(save=False)