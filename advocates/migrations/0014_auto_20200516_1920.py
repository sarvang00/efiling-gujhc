# Generated by Django 3.0.3 on 2020-05-16 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0013_auto_20200516_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='respond_to_case',
        ),
        migrations.AddField(
            model_name='response',
            name='affidavit_in_response',
            field=models.FileField(blank=True, null=True, upload_to='filings/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='response',
            name='further_affidavit',
            field=models.FileField(blank=True, null=True, upload_to='filings/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='response',
            name='othFile',
            field=models.FileField(blank=True, null=True, upload_to='filings/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='response',
            name='respond_to_case_number',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='response',
            name='respond_to_case_type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='response',
            name='respond_to_case_year',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='response',
            name='ruled_matter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='response',
            name='vnamFile',
            field=models.FileField(default='', upload_to='filings/%Y/%m/%d/'),
        ),
    ]
