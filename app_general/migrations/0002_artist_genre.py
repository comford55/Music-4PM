# Generated by Django 4.0.3 on 2022-03-28 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.CharField(choices=[('Classical', 'Classical'), ('Pop', 'Pop'), ('Rock', 'Rock'), ('R&B', 'R&B'), ('Soul', 'Soul'), ('Electronic', 'Electronic'), ('Jazz', 'Jazz'), ('Blue', 'Blue')], default='Pop', max_length=20),
        ),
    ]
