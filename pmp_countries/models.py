from django.db import models
from django.conf import settings

ENTRY_STATUS_CHOICES = settings.ENTRY_STATUS_CHOICES

YESNO_CHOICES = (
        (False, u'NO'),
        (True, u'YES'),
    )

class Country(models.Model):
    name = models.CharField(max_length=30, help_text=u'Name of the Country e.g Uganda')
    iso_code = models.CharField(max_length=5, help_text=u'iso code e.g Uganda == UG')
    contact_persons = models.TextField(help_text=u'Contact person(s)')
    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
    
    
    class Meta:
        verbose_name_plural = 'Countries'
    
    def __unicode__(self):
        return self.name

#class CapacityAssessment(models.Model):
#    assessment = models.TextField(help_text=u'Capacity Assessment Recommendations')
#    assessment_date = models.DateField(help_text=u'Date of assessment')
#    source = models.CharField(max_length=120, help_text=u'Source of this information')
#    remarks = models.TextField(help_text=u'Observations/Remarks on data')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#class TobaccoConsumption(models.Model):
#    """
#    Impact Indicator: Reduced tobacco consumption in target countries.
#    """
#    PRODUCT_TYPE_CHOICES = (
#        (u'cigarette', u'Cigarettes'),
#        (u'other_tobacco', u'Other tobacco products'),
#    )
#
#    GENDER_CHOICES = (
#        (u'm', u'Male'),
#        (u'f', u'Female')
#    )
#
#    AGE_RANGE_CHOICES = (
#        (u'u15', u'under 15 years'),
#        (u'o15', u'15 years and above')
#    )
#    product_type = models.CharField(max_length=15, choices=PRODUCT_TYPE_CHOICES, help_text=u'Type of tobacco product')
#    consumption_value = models.IntegerField(help_text=u'Consumption value')
#    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, help_text=u'Gender')
#    age_range = models.CharField(max_length=3, choices=AGE_RANGE_CHOICES, help_text=u'Age ranges')
#    assessment_date = models.DateField(help_text=u'Date of assessment')
#    source = models.CharField(max_length=120, help_text=u'Source of this information')
#    remarks = models.TextField(help_text=u'Observations/Remarks on data')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'Reduced Tobacco Consumption'
#
#    def __unicode__(self):
#        return '%s %s' % (self.product_type, self.consumption_value)
#
#class FctcArticle(models.Model):
#    ARTICLE_TYPE_CHOICES = (
#        (u'article6', u'Article 6: Tobacco taxes and price '),
#        (u'article8', u'Article 8: Smoke-free environments '),
#        (u'article11', u'Article 11: Packaging and Labeling '),
#        (u'article13', u'Article 13: Bans on advertising '),
#        (u'article15', u'Article 15: Illicit trade '),
#        (u'article17', u'Article 17: Alternative livelihoods '),
#        (u'other', u'Other (Please Specify) '),
#    )
#    article_name = models.CharField(max_length=12, choices=ARTICLE_TYPE_CHOICES, help_text=u'WHO FCTC Articles')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    def __unicode__(self):
#        return '%s' % self.article_name
#
#class FctcArticleImplementation(models.Model):
#    """
#    Outcome Indicators: 0.2-0.3 Implementation of WHO FCTC Guidelines
#    """
#    year = models.IntegerField(help_text=u'Year e.g 2010')
#    baseline = models.ForeignKey(CapacityAssessment, help_text=u'Baseline - CAR')
#    fctc_article = models.ForeignKey(FctcArticle, help_text=u'WHO FCTC Article')
#    drafted = models.BooleanField(choices=YESNO_CHOICES, help_text=u'FCTC compliant legislation drafted - Yes/No')
#    passed = models.BooleanField(choices=YESNO_CHOICES, help_text=u'FCTC compliant legislation passed - Yes/No')
#    adopted = models.BooleanField(choices=YESNO_CHOICES, help_text=u'FCTC compliant policy adopted - Yes/No')
#    developed = models.BooleanField(choices=YESNO_CHOICES, help_text=u'Policy action plan developed/financed - Yes/No')
#    enforced = models.BooleanField(choices=YESNO_CHOICES, help_text=u'Policy/Law enforced - Yes/No')
#    remarks = models.TextField(help_text=u'Observations/Remarks on data')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'WHO FCTC Article Implementation'
#
#    def __unicode__(self):
#        return '%s %s-%s' % (self.fctc_article, u'Drafted', self.drafted)
#
#class FacilityType(models.Model):
#    FACILITY_TYPE_CHOICES = (
#        (u'hospitals', u'Health care facilities '),
#        (u'schools', u'Educational facilities '),
#        (u'gov_offices', u'Government facilities '),
#        (u'indoor_offices', u'Indoor offices '),
#        (u'restaurants', u'Restaurants '),
#        (u'hotels', u'Hotels '),
#        (u'pubs', u'Pubs, bars, and night clubs '),
#        (u'transport', u'Public transport '),
#        (u'recreational', u'Recreational places '),
#        (u'all_others', u'All other public places '),
#    )
#    facility_type = models.CharField(max_length=15, choices=FACILITY_TYPE_CHOICES, help_text=u'Facilities')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'Facilities'
#
#    def __unicode__(self):
#        return '%s' % self.facility_type
#
#class PolicyImplementation(models.Model):
#    """
#    Outcome Indicator O.3 Increased implementation and enforcement of policies,
#    legislation in compliance with WHO FCTC guidelines
#
#    Level of compliance with FCTC Article 8 -- Enforcing Smoke-free  Environments
#    """
#    facility_type = models.ForeignKey(FacilityType, help_text=u'Facility/Places')
#    percentage = models.IntegerField(max_length=3, help_text=u'Percentage')
#    year = models.IntegerField(help_text=u'Year e.g 2010')
#    source = models.CharField(max_length=120, help_text=u'Source of this information')
#    remarks = models.TextField(help_text=u'Observations/Remarks on data')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'Level of compliance with FCTC Article 8'
#
#    def __unicode__(self):
#        return '%s - %s%s' % (self.facility_type, self.percentage, '%')
#
#class TaxesOnTobacco(models.Model):
#    TOBACCO_TYPE_CHOICES = (
#        (1, u'Tobacco sales (volume)'),
#        (2, u'Revenue from tobacco taxes'),
#        (3, u'Tobacco Excise Tax on price'),
#        (4, u'Tobacco Levy'),
#        (5, u'Average retail cost of package of cigarettes (20)'),
#    )
#    tax_type = models.CharField(max_length=15, choices=TOBACCO_TYPE_CHOICES, help_text=u'Tax')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'Taxes Levied on Tobacco'
#
#    def __unicode__(self):
#        return '%s' % self.tax_type
#
#class TobaccoTax(models.Model):
#    """
#    Outcome Indicator O.4 Increased tax on tobacco
#    """
#    tax = models.ForeignKey(TaxesOnTobacco, help_text=u'Tax')
#    value = models.IntegerField(help_text=u'Statistic')
#    year = models.IntegerField(help_text=u'Year e.g 2010')
#    source = models.CharField(max_length=120, help_text=u'Source of this information')
#    remarks = models.TextField(help_text=u'Observations/Remarks on data')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'Outcome Indicator O.4 Increased tax on tobacco'
#
#    def __unicode__(self):
#        return '%s - %s' % (self.tax, self.value)
#
#class LabelingType(models.Model):
#
#    LABELING_TYPE_CHOICES = (
#        (1, u'Graphic warnings'),
#        (2, u'Text warning'),
#        (3, u'Plain packaging (without brand)'),
#        (4, u'Use of misleading terms and descriptions'),
#    )
#    labeling_type = models.CharField(max_length=15, choices=LABELING_TYPE_CHOICES, help_text=u'Packaging/Labeling')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'Packaging and Labeling Types'
#
#    def __unicode__(self):
#        return '%s' % self.labeling_type
#
#class PackageAndLabel(models.Model):
#    """
#    Level of compliance with FCTC  Article 11 -- Packaging and Labeling
#    """
#    package_label = models.ForeignKey(LabelingType, help_text=u'Packaging and Labeling')
#    percentage = models.IntegerField(help_text=u'Percentage e.g 89.4')
#    year = models.IntegerField(help_text=u'Year e.g 2010')
#    source = models.CharField(max_length=120, help_text=u'Source of this information')
#    remarks = models.TextField(help_text=u'Observations/Remarks on data')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'Implementation of policies on packaging and labeling'
#
#    def __unicode__(self):
#        return '%s - %s%s' % (self.package_label, self.percentage, '%')
#
#class AdvertisingType(models.Model):
#
#    ADVERTISING_TYPE_CHOICES = (
#        (1, u'Advertising on billboards'),
#        (2, u'Advertising on points of sale'),
#        (3, u'Advertising on media (radio, TV, print)'),
#        (4, u'Corporate Social responsibility'),
#        (5, u'Event promotions'),
#        (6, u'Sponsorships'),
#        (7, u'Cross-border advertising'),
#    )
#    advertising_type = models.CharField(max_length=15, choices=ADVERTISING_TYPE_CHOICES, help_text=u'Advertising Type')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'Forms of Advertising'
#
#    def __unicode__(self):
#        return '%s' % self.advertising_type
#
#class AdvertisingBan(models.Model):
#    """
#    Outcome Indicator O.3 Increased implementation and enforcement of policies related to ban on advertising
#    Level of compliance with FCTC Article13 - Bans on advertising
#    """
#    advertising_type = models.ForeignKey(AdvertisingType, help_text=u'Advertising Type')
#    implemented = models.BooleanField(choices=YESNO_CHOICES, help_text=u'Yes/No')
#    year = models.IntegerField(help_text=u'Year e.g 2010')
#    source = models.CharField(max_length=120, help_text=u'Source of this information')
#    remarks = models.TextField(help_text=u'Observations/Remarks on data')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'Implementation of policies related to ban on advertising'
#
#    def __unicode__(self):
#        return '%s - %s' % (self.advertising_type, self.implemented)
#
#class IllicitTradeType(models.Model):
#
#    ILLICIT_TYPE_CHOICES = (
#        (1, u'Tracking and tracing illicit trade'),
#        (2, u'Inter-country collaboration'),
#        (3, u'Customs reports on what has been captured'),
#        (4, u'Forfeiture of illicit tobacco'),
#    )
#    illicit_trade_collaboration_type = models.CharField(max_length=15, choices=ILLICIT_TYPE_CHOICES, help_text=u'Illicit Trade Collaboration')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'Illicit Trade Collaboration'
#
#    def __unicode__(self):
#        return '%s' % self.illicit_trade_collaboration_type
#
#class IllicitTrade(models.Model):
#    """
#    Outcome Indicator O.3 Increased implementation and enforcement of policies related to illicit trade
#    Level of compliance with FCTC Article 15 - illicit trade
#    """
#    illicit_trade_type = models.ForeignKey(IllicitTradeType, help_text=u'Article 15 - Illicit Trade Type')
#    implemented = models.BooleanField(choices=YESNO_CHOICES, help_text=u'Yes/No')
#    year = models.IntegerField(help_text=u'Year e.g 2010')
#    source = models.CharField(max_length=120, help_text=u'Source of this information')
#    remarks = models.TextField(help_text=u'Observations/Remarks on data')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'Implementation of policies related to illicit trade'
#
#    def __unicode__(self):
#        return '%s - %s' % (self.illicit_trade_type, self.implemented)
#
#class LivelihoodType(models.Model):
#
#    LIVELIHOOD_TYPE_CHOICES = (
#        (1, u'On-Farm changes from tobacco to other products'),
#        (2, u'Off-farm changes - leaving tobacco to do other types of work (agricultural or non-agricultural)'),
#        (3, u'Marketing'),
#        (4, u'Education (health implications of tobacco)'),
#        (5, u'Value chain analysis of alternative livelihood'),
#    )
#    livelihood_type = models.CharField(max_length=15, choices=LIVELIHOOD_TYPE_CHOICES, help_text=u'FCTC Article 17 - Alternative Livelihoods')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'FCTC Article 17 - Alternative Livelihoods'
#
#    def __unicode__(self):
#        return '%s' % self.livelihood_type
#
#class AlternativeLivelihood(models.Model):
#    """
#    Outcome Indicator O.3 Increased implementation and enforcement of policies related to alternative livelihoods
#    Level of compliance with FCTC Article 17 - Alternative Livelihoods
#    """
#    livelihood_type = models.ForeignKey(LivelihoodType, help_text=u'FCTC Article 17 - Alternative Livelihoods')
#    implemented = models.BooleanField(choices=YESNO_CHOICES, help_text=u'Yes/No')
#    year = models.IntegerField(help_text=u'Year e.g 2010')
#    source = models.CharField(max_length=120, help_text=u'Source of this information')
#    remarks = models.TextField(help_text=u'Observations/Remarks on data')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'Implementation of policies related to illicit trade'
#
#    def __unicode__(self):
#        return '%s - %s' % (self.livelihood_type, self.implemented)
#
#class NTCPlanItem(models.Model):
#
#    NTCPLAN_ITEMS_CHOICES = (
#        (1, u'Country strategic objectives'),
#        (2, u'Institutional framework'),
#        (3, u'Monitoring and evaluation'),
#        (4, u'Funding support'),
#        (5, u'Strategies and activities'),
#    )
#    ntc_plan_item = models.CharField(max_length=15, choices=NTCPLAN_ITEMS_CHOICES, help_text=u'National TC plan developed and implemented')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'National TC plan developed and implemented'
#
#    def __unicode__(self):
#        return '%s' % self.ntc_plan_item
#
#class NTCPlan(models.Model):
#    """
#    Outcome Indicator 0.5 - National Tobacco Control plan development and implemented
#    National TC plan developed and implemented
#    """
#    ntc_plan_item = models.ForeignKey(NTCPlanItem, help_text=u'National TC plan developed and implemented')
#    implemented = models.BooleanField(choices=YESNO_CHOICES, help_text=u'Yes/No')
#    year = models.IntegerField(help_text=u'Year e.g 2010')
#    source = models.CharField(max_length=120, help_text=u'Source of this information')
#    remarks = models.TextField(help_text=u'Observations/Remarks on data')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'National TC plan developed and implemented'
#
#    def __unicode__(self):
#        return '%s - %s' % (self.ntc_plan_item, self.implemented)
#
#class NTCPlanArea(models.Model):
#
#    NTCPLAN_AREA_CHOICES = (
#        (1, u'TC issues in MCH'),
#        (2, u'TC issues in HIV / AIDS'),
#        (3, u'TC issues in TB'),
#        (4, u'TC issues in poverty reduction'),
#    )
#    ntc_plan_area = models.CharField(max_length=15, choices=NTCPLAN_AREA_CHOICES, help_text=u'National TC plan Area')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'National TC plan Area'
#
#    def __unicode__(self):
#        return '%s' % self.ntc_plan_area
#
#class TobaccoControl(models.Model):
#    """
#    Outcome Indicator 0.6 - Integration of TC - Tobacco Control into other areas
#    National TC plan developed and implemented
#    """
#    ntc_area = models.ForeignKey(NTCPlanItem, help_text=u'National TC plan developed and implemented')
#    implemented = models.BooleanField(choices=YESNO_CHOICES, help_text=u'Yes/No')
#    year = models.IntegerField(help_text=u'Year e.g 2010')
#    source = models.CharField(max_length=120, help_text=u'Source of this information')
#    remarks = models.TextField(help_text=u'Observations/Remarks on data')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#    class Meta:
#        verbose_name_plural = 'National TC plan Implemented In other Areas?'
#
#    def __unicode__(self):
#        return '%s - %s' % (self.ntc_area, self.implemented)
#
#class CountryProfile(models.Model):
#    """
#    Purpose of Country Profile: This tool is used to capture country level
#    evolution on tobacco control, partnerships, funding, use of CTCA services/products,
#    and outcomes that will serve to monitor the performance of the CTCA.
#    """
#    country = models.ForeignKey(Country)
#    capacity_assessment = models.ManyToManyField(CapacityAssessment, help_text=u'Capacity Assessment Recommendations', through='CountryCapacityAssessment')
#    tobacco_consumption_assessment = models.ManyToManyField(TobaccoConsumption, help_text=u'Impact Indicator: Reduced tobacco consumption in target countries', through='CountryReducedTobaccoConsumption')
#    fctc_article_implementation = models.ManyToManyField(FctcArticleImplementation, help_text=u'Outcome Indicators: 0.2-0.3 Implementation of WHO FCTC Guidelines', through='CountryFctcArticleImplementation')
#    policy_implementation = models.ManyToManyField(PolicyImplementation, help_text=u'Level of compliance with FCTC Article 8 -- Enforcing Smoke-free  Environments', through='CountryPolicyImplementation')
#    tobacco_tax = models.ManyToManyField(TobaccoTax, help_text=u'Increased tax on tobacco', through='CountryTobaccoTax')
#    package_label = models.ManyToManyField(PackageAndLabel, help_text=u'Level of compliance with FCTC  Article 11 - Packaging and Labeling', through='CountryPackageAndLabel')
#    advertising_ban = models.ManyToManyField(AdvertisingBan, help_text=u'Level of compliance with FCTC Article13 - Bans on advertising', through='CountryAdvertisingBan')
#    illicit_trade = models.ManyToManyField(IllicitTrade, help_text=u'Level of compliance with FCTC Article 15 - illicit trade', through='CountryIllicitTrade')
#    alternative_livelihood = models.ManyToManyField(AlternativeLivelihood, help_text=u'Level of compliance with FCTC Article 17 - Alternative Livelihoods', through='CountryAlternativeLivelihood')
#    ntc_plan = models.ManyToManyField(NTCPlan, help_text=u'National TC plan developed and implemented', through='CountryNTCPlan')
#    tobacco_control = models.ManyToManyField(TobaccoControl, help_text=u'National TC plan developed and implemented', through='CountryTobaccoControl')
#    entry_status = models.BooleanField(choices=ENTRY_STATUS_CHOICES, help_text=u'Approved/Un-approved')
#
#class CountryCapacityAssessment(models.Model):
#    country_profile = models.ForeignKey(CountryProfile)
#    capacity_assessment = models.ForeignKey(CapacityAssessment)
#
#    class Meta:
#        verbose_name_plural = 'Country Profile Capacity Assessment Recommendations'
#
#class CountryReducedTobaccoConsumption(models.Model):
#    country_profile = models.ForeignKey(CountryProfile)
#    tobacco_consumption = models.ForeignKey(TobaccoConsumption)
#
#    class Meta:
#        verbose_name_plural = 'Impact Indicator: Reduced tobacco consumption in target countries'
#
#class CountryFctcArticleImplementation(models.Model):
#    country_profile = models.ForeignKey(CountryProfile)
#    fctc_article_implementation = models.ForeignKey(FctcArticleImplementation)
#
#    class Meta:
#        verbose_name_plural = 'Outcome Indicators: 0.2-0.3 Implementation of WHO FCTC Guidelines'
#
#class CountryPolicyImplementation(models.Model):
#    country_profile = models.ForeignKey(CountryProfile)
#    policy_implementation = models.ForeignKey(PolicyImplementation)
#
#    class Meta:
#        verbose_name_plural = 'Level of compliance with FCTC Article 8 -- Enforcing Smoke-free  Environments'
#
#class CountryTobaccoTax(models.Model):
#    country_profile = models.ForeignKey(CountryProfile)
#    tobacco_tax = models.ForeignKey(TobaccoTax)
#
#    class Meta:
#        verbose_name_plural = 'Outcome Indicator O.4 Increased tax on tobacco'
#
#class CountryPackageAndLabel(models.Model):
#    country_profile = models.ForeignKey(CountryProfile)
#    package_label = models.ForeignKey(PackageAndLabel)
#
#    class Meta:
#        verbose_name_plural = 'Outcome Indicator O.3 Increased implementation and enforcement of policies related to packaging and labeling'
#
#class CountryAdvertisingBan(models.Model):
#    country_profile = models.ForeignKey(CountryProfile)
#    advertising_ban = models.ForeignKey(AdvertisingBan)
#
#    class Meta:
#        verbose_name_plural = 'Outcome Indicator O.3 Increased implementation and enforcement of policies related to ban on advertising'
#
#class CountryIllicitTrade(models.Model):
#    country_profile = models.ForeignKey(CountryProfile)
#    illicit_trade = models.ForeignKey(IllicitTrade)
#
#    class Meta:
#        verbose_name_plural = 'Outcome Indicator O.3 Increased implementation and enforcement of policies related to illicit trade'
#
#class CountryAlternativeLivelihood(models.Model):
#    country_profile = models.ForeignKey(CountryProfile)
#    alternative_livelhood = models.ForeignKey(AlternativeLivelihood)
#
#    class Meta:
#        verbose_name_plural = 'Outcome Indicator O.3 Increased implementation and enforcement of policies related to alternative livelihoods'
#
#class CountryNTCPlan(models.Model):
#    country_profile = models.ForeignKey(CountryProfile)
#    ntc_plan = models.ForeignKey(NTCPlan)
#
#    class Meta:
#        verbose_name_plural = 'Outcome Indicator 0.5 - National Tobacco Control plan development and implemented'
#
#class CountryTobaccoControl(models.Model):
#    country_profile = models.ForeignKey(CountryProfile)
#    tobacco_control = models.ForeignKey(TobaccoControl)
#
#    class Meta:
#        verbose_name_plural = 'Outcome Indicator 0.6 - Integration of TC - Tobacco Control into other areas'
