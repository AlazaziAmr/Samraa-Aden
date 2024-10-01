from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin, TranslatableTabularInline

from .models import Section, Agent, Branch

# Register your models here.

admin.site.site_header = _("Samra'a Aden Dashboard")
admin.site.site_title = _("Samra'a Aden Admin")


class InlineAgent(TranslatableTabularInline):
    model = Agent
    extra = 1


class InlineBranch(TranslatableTabularInline):
    model = Branch
    extra = 1


@admin.register(Section)
class SectionAdmin(TranslatableAdmin):
    inlines = [InlineAgent, InlineBranch]
    fieldsets = [
        (
            _('SEO'),
            {
                "fields": ['page_title', 'page_description'],
            },
        ),
        (
            _('cover'),
            {
                "fields": ['bg_image', 'bg_description', 'twitter', 'facebook', 'instagram', 'youtube'],
            },
        ),
        (
            _('cards'),
            {
                "fields": ['card1', 'card2', 'card3', 'card4'],
            },
        ),
        (
            _('about_us'),
            {
                "fields": ['about_us', 'our_goal_text', 'our_vision_text', 'our_message_text', 'about_our_categories',
                           'about_us_bg_image', 'our_goal_image', 'our_vision_image', 'our_message_image',
                           'our_categories_image'],
            },
        ),
        (
            _('contact_us'),
            {
                "fields": ['address', 'work_days', 'work_from', 'work_to', 'phone1', 'phone2', 'email1', 'email2'],
            },
        ),
        (
            None,
            {
                "fields": ['active'],
            }
        ),
    ]
    list_display = ('page_title', 'active')
    list_filter = ('active',)
