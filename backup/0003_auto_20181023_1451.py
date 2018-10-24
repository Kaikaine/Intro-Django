# Generated by Django 2.1.2 on 2018-10-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20181022_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.AddField(
            model_name='person',
            name='blood_type',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]