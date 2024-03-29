from django.db import models
from django.conf import settings
from datetime import datetime

from django.core.validators import FileExtensionValidator


class Filing(models.Model):
    filing_advocate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    sanat_number = models.CharField(max_length=15)
    advocate_hc_code = models.CharField(max_length=10)
    filing_case = models.CharField(max_length=20, blank=True)
    rules = models.TextField()
    matter_type = models.CharField(max_length=10) #Civil/Criminal
    bench_type = models.CharField(max_length=20)
    case_type = models.CharField(max_length=50)
    connected_case = models.BooleanField()
    connected_case_type = models.CharField(max_length=20, blank=True, default='')
    connected_case_number = models.IntegerField(blank=True, default=0)
    connected_case_year = models.IntegerField(blank=True, default=0)
    filing_urgency = models.BooleanField()
    urgencyFile = models.FileField(upload_to='filings/%Y/%m/%d/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    indexFile = models.FileField(upload_to='filings/%Y/%m/%d/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    LoEventsFile = models.FileField(upload_to='filings/%Y/%m/%d/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    synopsisFile = models.FileField(upload_to='filings/%Y/%m/%d/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    memoFile = models.FileField(upload_to='filings/%Y/%m/%d/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    pastFile = models.FileField(upload_to='filings/%Y/%m/%d/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    annexFile = models.FileField(upload_to='filings/%Y/%m/%d/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    vnamFile = models.FileField(upload_to='filings/%Y/%m/%d/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    othFile = models.FileField(upload_to='filings/%Y/%m/%d/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    filing_status = models.IntegerField(default=3)
    checklist_8 = models.BooleanField(default=True)
    checklist_9 = models.BooleanField(default=True)
    checklist_10 = models.BooleanField(default=True)
    checklist_11 = models.BooleanField(default=True)
    checklist_15 = models.BooleanField(default=True)
    checklist_16 = models.BooleanField(default=True)
    checklist_17 = models.BooleanField(default=True)
    checklist_21 = models.BooleanField(default=True)
    checklist_25 = models.BooleanField(default=True)
    checklist_31 = models.BooleanField(default=True)
    filing_comments = models.TextField(blank=True, default="Pending Review")
    filing_time = models.DateTimeField(default=datetime.now)
    officer_stamp = models.CharField(max_length=10, default='')

class Response(models.Model):
    responding_advocate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,)
    sanat_number = models.CharField(max_length=15)
    advocate_hc_code = models.CharField(max_length=10, default='')
    respond_to_case_type = models.CharField(max_length=50, default='')
    respond_to_case_number = models.IntegerField(blank=True, default=0)
    respond_to_case_year = models.IntegerField(blank=True, default=0)
    vnamFile = models.FileField(upload_to='filings/%Y/%m/%d/', default='', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    affidavit_in_response = models.FileField(upload_to='filings/%Y/%m/%d/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    further_affidavit = models.FileField(upload_to='filings/%Y/%m/%d/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    othFile = models.FileField(upload_to='filings/%Y/%m/%d/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    response_note = models.TextField(blank=True)
    response_status = models.IntegerField(default=3)
    ruled_matter = models.BooleanField(default=False)
    officer_stamp = models.CharField(max_length=10, default='')
    response_comments = models.TextField(blank=True, default="Pending Review")
    response_time = models.DateTimeField(default=datetime.now)