# Generated by Django 4.0.3 on 2022-03-28 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0005_alter_artist_genre_alter_song_albumid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='albumID',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='app_general.album'),
        ),
    ]
