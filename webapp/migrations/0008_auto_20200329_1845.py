# Generated by Django 3.0.4 on 2020-03-29 18:45

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_ngo_pincode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ngo',
            options={'verbose_name': 'NGO'},
        ),
        migrations.AlterModelOptions(
            name='ngoowner',
            options={'verbose_name': 'NGO Owner'},
        ),
        migrations.AlterModelOptions(
            name='ngouser',
            options={'verbose_name': 'NGO User'},
        ),
        migrations.AddField(
            model_name='ngo',
            name='special_needs_groups',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('no', 'No, we do not work with any special needs group'), ('mental_illness', 'People with mental illness'), ('hearing_loss', 'People with hearing loss'), ('physical_disabilities', 'People with physical disabilities'), ('intellectual_disabilities', 'People with intellectual disabilities'), ('aids', 'People living with HIV/AIDS'), ('chronic_illness', 'People living with chronic illness such as cancer, heart ailments, are immune-compromised'), ('elderly', 'Elderly'), ('tribal_population', 'Tribal population'), ('migrants', 'Migrants and internally displaced'), ('hospice_shelters', 'Hospice/homes/orphanages/shelters'), ('homeless', 'Homeless'), ('others', 'Others')], max_length=167, null=True),
        ),
        migrations.AddField(
            model_name='ngo',
            name='staff_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='ngouser',
            unique_together=set(),
        ),
    ]
