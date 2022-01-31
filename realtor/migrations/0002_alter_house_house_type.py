# Generated by Django 4.0.1 on 2022-01-31 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='house_type',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Lease', 'Lease'), ('Rent', 'Rent')], max_length=2000),
        ),
    ]