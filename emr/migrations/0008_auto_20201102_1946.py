# Generated by Django 3.1.2 on 2020-11-03 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0007_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]