# Generated by Django 5.2 on 2025-04-12 18:35

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_schoolclass_description_alter_teacher_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='title_en',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_uz',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='gallerycategory',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='gallerycategory',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='gallerycategory',
            name='name_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='hobby',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='hobby',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='hobby',
            name='name_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='description_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='food_en',
            field=models.CharField(max_length=50, null=True, verbose_name='food'),
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='food_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='food'),
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='food_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='food'),
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='name_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='science',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='science',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='science',
            name='name_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='skill',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='skill',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='skill',
            name='name_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='about_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='about teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='about_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='about teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='about_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='about teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='experience_en',
            field=models.CharField(max_length=255, null=True, verbose_name='experience'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='experience_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='experience'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='experience_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='experience'),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='weekday_en',
            field=models.CharField(max_length=50, null=True, verbose_name='weekday'),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='weekday_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='weekday'),
        ),
        migrations.AddField(
            model_name='teacherschedule',
            name='weekday_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='weekday'),
        ),
    ]
