from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from django.urls import reverse
from django_resized import ResizedImageField

# Create your models here.

class Section(TranslatableModel):
    translations = TranslatedFields(
    page_title = models.CharField(_('page_title'),max_length=60, help_text=_('page_title_help_text')),
    page_description = models.CharField(_('page_description'), help_text=_('page_description_help_text')),
    bg_description = models.TextField(_('bg_description'), help_text=_('bg_description_help_text')),
    card1 = models.CharField(_('card1'),max_length=25, help_text=_('cards_help_text')),
    card2 = models.CharField(_('card2'),max_length=25, help_text=_('cards_help_text')),
    card3 = models.CharField(_('card3'),max_length=25, help_text=_('cards_help_text')),
    card4 = models.CharField(_('card4'),max_length=25, help_text=_('cards_help_text')),
    about_us = models.TextField(_('about_us'), help_text=_('about_us_help_text')),
    our_goal_text = models.TextField(_('our_goal_text'), help_text=_('our_goal_help_text')),
    our_vision_text = models.TextField(_('our_vision_text'), help_text=_('our_vision_help_text')),
    our_message_text = models.TextField(_('our_message_text'), help_text=_('our_message_help_text')),
    about_our_categories = models.TextField(_('about_our_categories'), help_text=_('about_our_categories_help_text')),
    address = models.CharField(_('address'),max_length=100, help_text=_('address_help_text')),
    work_days = models.CharField(_('work_days'),max_length=25, help_text=_('work_days_help_text')),
    )
    twitter = models.URLField(_('twitter_url'))
    facebook = models.URLField(_('facebook_url'))
    instagram = models.URLField(_('instagram_url'))
    youtube = models.URLField(_('youtube_url'))
    phone1 = PhoneNumberField(_('phone1'), region='YE', max_length=16, help_text=_('phone_help_text'))
    phone2 = PhoneNumberField(_('phone2'), region='YE', max_length=16, help_text=_('phone_help_text'), null=True,blank=True)
    email1 = models.EmailField(_('email1'))
    email2 = models.EmailField(_('email2'), null=True, blank=True)
    work_from = models.TimeField(_('work_from'))
    work_to = models.TimeField(_('work_to'))
    bg_image = ResizedImageField(_('bg_image'), quality=90, force_format="WEBP", upload_to="images/home/")
    about_us_bg_image = ResizedImageField(_('about_us_bg_image'), quality=90, force_format="WEBP", upload_to="images/home/")
    our_goal_image = ResizedImageField(_('our_goal_image'), quality=90, force_format="WEBP", upload_to="images/home/")
    our_vision_image = ResizedImageField(_('our_vision_image'), quality=90, force_format="WEBP", upload_to="images/home/")
    our_message_image = ResizedImageField(_('our_message_image'), quality=90, force_format="WEBP", upload_to="images/home/")
    our_categories_image = ResizedImageField(_('our_categories_image'), quality=90, force_format="WEBP", upload_to="images/home/")
    active = models.BooleanField(_('active'), default=True)
    def __str__(self):
        return self.page_title
    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = _('home_page')
        verbose_name_plural = _('home_page')
        ordering = ['id']

class Agent(TranslatableModel):
    translations = TranslatedFields(
    name = models.CharField(_('agent_name'),max_length=50, help_text=_('agent_name_help_text')),
    address = models.CharField(_('address'),max_length=100, help_text=_('address_help_text')),
    description = models.TextField(_('agent_description'),max_length=500, help_text=_('agent_description_help_text')),
    )
    image = ResizedImageField(_('agent_image'), quality=90, force_format="WEBP", upload_to="images/agents/")
    section = models.ForeignKey(Section,on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('agent')
        verbose_name_plural = _('agents')

class Branch(TranslatableModel):
    translations = TranslatedFields(
    name = models.CharField(_('branch_name'),max_length=100, help_text=_('branch_name_help_text')),
    address = models.CharField(_('address'),max_length=255, help_text=_('branch_address_help_text')),
    )
    image = ResizedImageField(_('branch_image'), quality=90, force_format="WEBP", upload_to="images/branches/")
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('branch')
        verbose_name_plural = _('branches')

@receiver(models.signals.post_delete, sender=Section)
def delete_Home_images(sender, instance, **kwargs):
    instance.bg_image.delete(save=False)
    instance.about_us_bg_image.delete(save=False)
    instance.our_goal_image.delete(save=False)
    instance.our_vision_image.delete(save=False)
    instance.our_message_image.delete(save=False)

@receiver(models.signals.post_delete, sender=Agent)
def delete_Agent_images(sender, instance, **kwargs):
    instance.image.delete(save=False)

@receiver(models.signals.post_delete, sender=Branch)
def delete_Branch_images(sender, instance, **kwargs):
    instance.image.delete(save=False)