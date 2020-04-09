# Generated by Django 3.0.4 on 2020-04-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_auto_20200408_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='operational_districts',
            field=models.ManyToManyField(through='webapp.NgoDistrict', to='webapp.District'),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='does_staff_use_phones',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=''),
        ),
    ]