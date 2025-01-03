# Generated by Django 4.2.17 on 2024-12-15 20:09

from django.db import migrations, models
import django_countries.fields
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birth_country', django_countries.fields.CountryField(max_length=2)),
                ('birth_date', models.DateField()),
                ('biography', djrichtextfield.models.RichTextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('photo_url', models.URLField(blank=True, max_length=1024, null=True)),
            ],
        ),
    ]
