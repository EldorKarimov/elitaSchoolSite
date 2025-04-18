# Generated by Django 5.2 on 2025-04-12 17:44

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('content', models.TextField(verbose_name='content')),
                ('image', models.ImageField(upload_to='media/news/images', verbose_name='image')),
                ('is_published', models.BooleanField(default=False, verbose_name='published')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='news.newscategory', verbose_name='category')),
                ('tags', models.ManyToManyField(to='news.tag', verbose_name='tag')),
            ],
            options={
                'verbose_name': 'new',
                'verbose_name_plural': 'news',
            },
        ),
    ]
