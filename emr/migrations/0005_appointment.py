# Generated by Django 3.1.2 on 2020-10-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0004_patient_medical_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('visitor_name', models.CharField(blank=True, max_length=254)),
                ('description', models.TextField(blank=True)),
                ('date_time', models.DateTimeField(blank=True)),
            ],
        ),
    ]
