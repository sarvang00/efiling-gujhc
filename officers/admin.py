from django.contrib import admin

from .models import Case

class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'case_type', 'case_number', 'case_year', 'bench_type',)
    list_display_links = ('id',)
    list_filter = ('case_type', 'case_year', 'bench_type',)
    search_fields = ('case_type', 'case_number', 'case_year', 'bench_type',)
    list_per_page = 25

admin.site.register(Case, CaseAdmin)
