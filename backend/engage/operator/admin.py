from django.contrib import admin
from django.forms import ModelForm
from jet.admin import CompactInline

from .models import (
    Operator,
    OperatorAd,
    OperatorFaq,
    OperatorWebsite,
    OperatorHomeSection,
    Region,
    PurchaseCoin,
    RedeemPackage
)
from ..core.fields import SVGAndImageFormField


class OperatorHomeSectionModelForm(ModelForm):
    class Meta:
        model = OperatorHomeSection
        exclude = []
        field_classes = {
            'icon': SVGAndImageFormField,
        }


class OperatorFaqInline(CompactInline):
    model = OperatorFaq


class OperatorWebsiteInline(admin.StackedInline):
    model = OperatorWebsite
    min_num = 1
    max_num = 1


class OperatorHomeSectionInline(CompactInline):
    model = OperatorHomeSection
    form = OperatorHomeSectionModelForm
    show_change_link = True
    can_delete = True
    min_num = 1


class PurchaseCoinInline(CompactInline):
    model = PurchaseCoin
    exclude = ('uid',)
    min_num = 1


class RedeemPackageInline(CompactInline):
    model = RedeemPackage
    exclude = ('uid',)
    min_num = 1


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'created')
    exclude = ('schema',)
    inlines = [
        OperatorWebsiteInline,
        OperatorHomeSectionInline,
        OperatorFaqInline,
        RedeemPackageInline,
        PurchaseCoinInline,
    ]

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        extra_context['show_delete'] = False
        return super().change_view(request, object_id, form_url,
                                   extra_context=extra_context)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'default_language', 'default_currency', 'created', 'modified')


@admin.register(OperatorAd)
class OperatorAdAdmin(admin.ModelAdmin):
    list_display = ('name', 'ad_type', 'start_date', 'end_date', 'created', 'modified')
