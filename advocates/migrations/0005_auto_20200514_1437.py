# Generated by Django 3.0.3 on 2020-05-14 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0004_auto_20200514_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='respond_to_case_id',
            new_name='respond_to_case',
        ),
    ]
