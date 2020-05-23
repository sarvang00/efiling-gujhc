# Generated by Django 3.0.3 on 2020-05-13 16:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('advocates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_type', models.CharField(max_length=20)),
                ('case_number', models.IntegerField()),
                ('case_year', models.IntegerField()),
                ('bench_type', models.CharField(max_length=50)),
                ('case_registration', models.DateTimeField(default=datetime.datetime.now)),
                ('filing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='advocates.Filing')),
            ],
        ),
    ]
