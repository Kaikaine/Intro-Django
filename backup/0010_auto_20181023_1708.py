# Generated by Django 2.1.2 on 2018-10-23 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20181023_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='blood_type',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]