# Generated by Django 4.0.4 on 2022-05-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_patient_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
