# Generated by Django 5.0.1 on 2024-01-07 15:22

import autoslug.fields
import slugify
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0007_remove_comments_comment_genre_slug_movie_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', slugify=slugify.slugify, unique=True),
        ),
    ]
