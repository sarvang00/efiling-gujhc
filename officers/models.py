from django.db import models
from datetime import datetime

from advocates.models import Filing

class Case(models.Model):
    filing = models.ForeignKey(Filing, on_delete=models.DO_NOTHING)
    case_type = models.CharField(max_length=50, default='')
    case_number = models.IntegerField(blank=True, default=0)
    case_year = models.IntegerField(blank=True, default=0)
    bench_type = models.CharField(max_length=50)
    case_registration = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.case_type+'/'+self.case_number+'/'+self.case_year