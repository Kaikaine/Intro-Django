# Generated by Django 2.1.2 on 2018-10-25 22:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('primary', models.CharField(choices=[('----', 'None'), ('NOR', 'Normal'), ('FIR', 'Fire'), ('WAT', 'Water'), ('ELE', 'Electric'), ('GRA', 'Grass'), ('ICE', 'Ice'), ('FIG', 'Fighting'), ('POI', 'POISON'), ('GRO', 'Ground'), ('FLY', 'Flying'), ('PSY', 'Psychic'), ('BUG', 'Bug'), ('ROC', 'Rock'), ('GHO', 'Ghost'), ('DRA', 'Dragon'), ('DAR', 'Dark'), ('STE', 'Steel'), ('FAI', 'Fairy')], max_length=20)),
                ('secondary', models.CharField(choices=[('----', 'None'), ('NOR', 'Normal'), ('FIR', 'Fire'), ('WAT', 'Water'), ('ELE', 'Electric'), ('GRA', 'Grass'), ('ICE', 'Ice'), ('FIG', 'Fighting'), ('POI', 'POISON'), ('GRO', 'Ground'), ('FLY', 'Flying'), ('PSY', 'Psychic'), ('BUG', 'Bug'), ('ROC', 'Rock'), ('GHO', 'Ghost'), ('DRA', 'Dragon'), ('DAR', 'Dark'), ('STE', 'Steel'), ('FAI', 'Fairy')], max_length=20)),
                ('about', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
