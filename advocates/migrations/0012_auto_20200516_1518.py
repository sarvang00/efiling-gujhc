# Generated by Django 3.0.3 on 2020-05-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0011_auto_20200516_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filing',
            name='annexFile',
            field=models.FileField(blank=True, default='', null=True, upload_to='filings/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='filing',
            name='othFile',
            field=models.FileField(blank=True, default='', null=True, upload_to='filings/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='filing',
            name='urgencyFile',
            field=models.FileField(blank=True, default='', null=True, upload_to='filings/%Y/%m/%d/'),
        ),
    ]
