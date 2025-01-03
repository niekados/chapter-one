# Generated by Django 4.2.17 on 2025-01-03 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_alter_book_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='library', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Library Entries',
                'ordering': ['-purchase_date'],
                'unique_together': {('user', 'book')},
            },
        ),
    ]
