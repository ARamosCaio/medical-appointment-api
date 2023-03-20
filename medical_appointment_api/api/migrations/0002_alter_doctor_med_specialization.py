# Generated by Django 4.1.7 on 2023-03-20 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='med_specialization',
            field=models.CharField(choices=[('OR', 'Orthopedist'), ('OP', 'Ophthalmologist'), ('GP', 'General Practitioner')], max_length=2),
        ),
    ]