# Generated by Django 3.2.8 on 2022-10-04 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000000)),
                ('location', models.CharField(max_length=10000000)),
                ('time', models.CharField(max_length=10000000)),
                ('link', models.CharField(max_length=10000000)),
            ],
        ),
    ]
