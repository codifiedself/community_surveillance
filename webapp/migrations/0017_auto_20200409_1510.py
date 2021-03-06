# Generated by Django 3.0.4 on 2020-04-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_auto_20200409_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ngo',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='ngo',
            name='population_reach',
        ),
        migrations.AlterField(
            model_name='ngo',
            name='operational_districts',
            field=models.ManyToManyField(blank=True, through='webapp.NgoDistrict', to='webapp.District'),
        ),
    ]
