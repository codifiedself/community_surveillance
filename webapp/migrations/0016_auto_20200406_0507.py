# Generated by Django 3.0.4 on 2020-04-06 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20200406_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='does_staff_use_phones',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=''),
        ),
    ]