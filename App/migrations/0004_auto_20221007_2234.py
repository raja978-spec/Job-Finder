# Generated by Django 3.2.8 on 2022-10-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_internshipjobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultjobs',
            name='caption',
            field=models.CharField(default='', max_length=10000000),
        ),
        migrations.AddField(
            model_name='jobs',
            name='caption',
            field=models.CharField(default='', max_length=10000000),
        ),
    ]
