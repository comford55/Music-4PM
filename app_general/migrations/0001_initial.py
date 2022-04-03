# Generated by Django 4.0.3 on 2022-03-27 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('albumID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('albumName', models.CharField(max_length=50)),
                ('releaseDate', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artistID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('artistName', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('picture', models.ImageField(blank=True, default=None, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songID', models.CharField(max_length=10)),
                ('songName', models.CharField(max_length=50)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('albumID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_general.album')),
                ('artistID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_general.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlistName', models.CharField(default='New Playlist', max_length=50)),
                ('song', models.ManyToManyField(to='app_general.song')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artistID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_general.artist'),
        ),
    ]
