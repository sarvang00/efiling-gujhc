# Generated by Django 3.0.3 on 2020-05-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0016_auto_20200516_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='advocate_hc_code',
            field=models.CharField(default='', max_length=10),
        ),
    ]
