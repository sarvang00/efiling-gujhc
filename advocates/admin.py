from django.contrib import admin

from .models import Filing, Response

class FilingAdmin(admin.ModelAdmin):
    list_display = ('id', 'advocate_hc_code', 'filing_case', 'filing_status', 'matter_type', 'bench_type', 'case_type', 'officer_stamp')
    list_display_links = ('id',)
    list_filter = ('advocate_hc_code', 'filing_case', 'filing_status', 'matter_type', 'bench_type', 'case_type', 'officer_stamp')
    search_fields = ('advocate_hc_code', 'filing_status', 'bench_type', 'case_type', 'officer_stamp')
    list_per_page = 25

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'advocate_hc_code', 'respond_to_case_type', 'respond_to_case_number', 'respond_to_case_year', 'response_status', 'officer_stamp')
    list_display_links = ('id',)
    list_filter = ('advocate_hc_code', 'respond_to_case_type', 'respond_to_case_year', 'response_status', 'officer_stamp')
    search_fields = ('advocate_hc_code', 'respond_to_case_type', 'respond_to_case_year', 'case_type',)
    list_per_page = 25

admin.site.register(Filing, FilingAdmin)

admin.site.register(Response, ResponseAdmin)