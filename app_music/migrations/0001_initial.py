# Generated by Django 4.0.3 on 2022-03-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artistID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('artName', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=10)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='artistIMG/')),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
