# Generated by Django 4.2.17 on 2025-01-02 19:57

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_remove_author_photo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='biography',
            field=djrichtextfield.models.RichTextField(blank=True, null=True),
        ),
    ]
