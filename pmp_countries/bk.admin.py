'''
Created on Feb 19, 2012

@author: asseym
'''
from .models import *
from django.contrib import admin
from pmp_partnerships.models import Operations

class HiddenModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, *args, **kwargs):
        perms = admin.ModelAdmin.get_model_perms(self, *args, **kwargs)
        perms['hide_model'] = True
        return perms
    
class OperationInline(admin.TabularInline):
    model = Operations
    extra = 2

#class CapacityAssessmentAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['assessment', 'assessment_date', 'source', 'remarks']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#    list_display = ('assessment_date', 'source')
#    list_filter = ['assessment_date']
#    search_fields = ['assessment', 'source']
#
#class TobaccoConsumptionAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['product_type', 'consumption_value', 'gender', 'age_range', 'assessment_date','source', 'remarks']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#    list_display = ('product_type', 'consumption_value', 'gender', 'age_range', 'assessment_date', 'source')
#    list_filter = ['assessment_date']
#    search_fields = ['product_type', 'gengder', 'source']
#
#class FctcArticleAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['article_name']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class FctcArticleImplementationAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['year', 'baseline', 'fctc_article', 'drafted', 'passed', 'adopted', 'developed', 'enforced']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class FacilityTypeAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['facility_type']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class PolicyImplementationAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['facility_type', 'percentage', 'year', 'source', 'remarks']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class TaxesOnTobaccoAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['tax_type']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class TobaccoTaxAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['tax', 'value', 'year', 'source', 'remarks']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class LabelingTypeAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['labeling_type']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class PackageAndLabelAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['package_label', 'percentage', 'year', 'source', 'remarks']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class AdvertisingTypeAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['advertising_type']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class AdvertisingBanAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['advertising_type', 'implemented', 'year', 'source', 'remarks']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class IllicitTradeTypeAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['illicit_trade_collaboration_type']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class IllicitTradeAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['illicit_trade_type', 'implemented', 'year', 'source', 'remarks']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class LivelihoodTypeAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['livelihood_type']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class AlternativeLivelihoodAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['livelihood_type', 'implemented', 'year', 'source', 'remarks']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class NTCPlanItemAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['ntc_plan_item']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class NTCPlanAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['ntc_plan_item', 'implemented', 'year', 'source', 'remarks']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class NTCPlanAreaAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['ntc_plan_area']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#class TobaccoControlAdmin(HiddenModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['ntc_area', 'implemented', 'year', 'source', 'remarks']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
    
class CountryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'iso_code', 'contact_persons']}),
        ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'iso_code', 'contact_persons', 'entry_status')
    list_filter = ['iso_code']
    search_fields = ['name']
    list_per_page = 20
    inlines = [OperationInline]

#class CountryCapacityAssessmentInline(admin.TabularInline):
#    model = CountryCapacityAssessment
#    extra = 2
#
#class CountryReducedTobaccoConsumptionInline(admin.TabularInline):
#    model = CountryReducedTobaccoConsumption
#    extra = 2
#
#class CountryFctcArticleImplementationInline(admin.TabularInline):
#    model = CountryFctcArticleImplementation
#    extra = 2
#
#class CountryPolicyImplementationInline(admin.TabularInline):
#    model = CountryPolicyImplementation
#    extra = 2
#
#class CountryTobaccoTaxInline(admin.TabularInline):
#    model = CountryTobaccoTax
#    extra = 2
#
#class CountryPackageAndLabelInline(admin.TabularInline):
#    model = CountryPackageAndLabel
#    extra = 2
#
#class CountryAdvertisingBanInline(admin.TabularInline):
#    model = CountryAdvertisingBan
#    extra = 2
#
#class CountryIllicitTradeInline(admin.TabularInline):
#    model = CountryIllicitTrade
#    extra = 2
#
#class CountryAlternativeLivelihoodInline(admin.TabularInline):
#    model = CountryAlternativeLivelihood
#    extra = 2
#
#class CountryNTCPlanInline(admin.TabularInline):
#    model = CountryNTCPlan
#    extra = 2
#
#class CountryTobaccoControlInline(admin.TabularInline):
#    model = CountryTobaccoControl
#    extra = 2
#
#class CountryProfileAdmin(admin.ModelAdmin):
#    fieldsets = [
#                    (None,     {'fields':['country']}),
#                    ('Publication Status', {'fields': ['entry_status'], 'classes': ['collapse']}),
#    ]
#
#    inlines = [
#            CountryCapacityAssessmentInline,
#            CountryReducedTobaccoConsumptionInline,
#            CountryFctcArticleImplementationInline,
#            CountryPolicyImplementationInline,
#            CountryTobaccoTaxInline,
#            CountryPackageAndLabelInline,
#            CountryAdvertisingBanInline,
#            CountryIllicitTradeInline,
#            CountryAlternativeLivelihoodInline,
#            CountryNTCPlanInline,
#            CountryTobaccoControlInline,
#    ]

#admin.site.register(CountryProfile, CountryProfileAdmin)
admin.site.register(Country, CountryAdmin)
#admin.site.register(FctcArticle, FctcArticleAdmin)
#admin.site.register(FacilityType, FacilityTypeAdmin)
#admin.site.register(CapacityAssessment, CapacityAssessmentAdmin)
#admin.site.register(TobaccoConsumption, TobaccoConsumptionAdmin)
#admin.site.register(FctcArticleImplementation, FctcArticleImplementationAdmin)
#admin.site.register(PolicyImplementation, PolicyImplementationAdmin)
#admin.site.register(TaxesOnTobacco, TaxesOnTobaccoAdmin)
#admin.site.register(TobaccoTax, TobaccoTaxAdmin)
#admin.site.register(LabelingType, LabelingTypeAdmin)
#admin.site.register(PackageAndLabel, PackageAndLabelAdmin)
#admin.site.register(AdvertisingType, AdvertisingTypeAdmin)
#admin.site.register(AdvertisingBan, AdvertisingBanAdmin)
#admin.site.register(IllicitTradeType, IllicitTradeTypeAdmin)
#admin.site.register(IllicitTrade, IllicitTradeAdmin)
#admin.site.register(LivelihoodType, LivelihoodTypeAdmin)
#admin.site.register(AlternativeLivelihood, AlternativeLivelihoodAdmin)
#admin.site.register(NTCPlanItem, NTCPlanItemAdmin)
#admin.site.register(NTCPlanArea, NTCPlanAreaAdmin)
#admin.site.register(TobaccoControl, TobaccoControlAdmin)