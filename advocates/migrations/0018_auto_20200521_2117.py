# Generated by Django 3.0.3 on 2020-05-21 15:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0017_response_advocate_hc_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filing',
            name='LoEventsFile',
            field=models.FileField(upload_to='filings/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='filing',
            name='annexFile',
            field=models.FileField(blank=True, null=True, upload_to='filings/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='filing',
            name='indexFile',
            field=models.FileField(upload_to='filings/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='filing',
            name='memoFile',
            field=models.FileField(upload_to='filings/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='filing',
            name='othFile',
            field=models.FileField(blank=True, null=True, upload_to='filings/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='filing',
            name='pastFile',
            field=models.FileField(upload_to='filings/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='filing',
            name='synopsisFile',
            field=models.FileField(upload_to='filings/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='filing',
            name='urgencyFile',
            field=models.FileField(blank=True, null=True, upload_to='filings/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='filing',
            name='vnamFile',
            field=models.FileField(upload_to='filings/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]