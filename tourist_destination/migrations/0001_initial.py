# Generated by Django 5.0.6 on 2024-05-23 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TouristDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100)),
                ('weather', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('google_map_link', models.URLField()),
                ('image', models.ImageField(upload_to='destinations/')),
                ('description', models.TextField()),
            ],
        ),
    ]