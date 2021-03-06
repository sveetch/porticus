# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-08 14:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields
import mptt.fields
import tagging.fields


def get_album_template_choices():
    return settings.PORTICUS_ALBUM_TEMPLATE_CHOICES


def get_album_template_default():
    return settings.PORTICUS_ALBUM_TEMPLATE_DEFAULT


def get_gallery_template_choices():
    return settings.PORTICUS_GALLERY_TEMPLATE_CHOICES


def get_gallery_template_default():
    return settings.PORTICUS_GALLERY_TEMPLATE_DEFAULT


def get_ressource_filetype_choices():
    return settings.PORTICUS_RESSOURCE_FILETYPE_CHOICES


def get_ressource_filetype_default():
    return settings.PORTICUS_RESSOURCE_FILETYPE_DEFAULT


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='created')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('publish', models.BooleanField(choices=[(True, 'Published'), (False, 'Unpublished')], default=True, verbose_name='published')),
                ('priority', models.IntegerField(default=100, verbose_name='display priority')),
                ('template_name', models.CharField(choices=get_album_template_choices(), default=get_album_template_default(), max_length=255, verbose_name='template')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', filebrowser.fields.FileBrowseField(blank=True, default=None, max_length=255, null=True, verbose_name='image')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
            ],
            options={
                'verbose_name': 'album',
                'verbose_name_plural': 'albums',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='created')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('publish', models.BooleanField(choices=[(True, 'Published'), (False, 'Unpublished')], default=True, verbose_name='published')),
                ('priority', models.IntegerField(default=100, verbose_name='display priority')),
                ('template_name', models.CharField(choices=get_gallery_template_choices(), default=get_gallery_template_default(), max_length=255, verbose_name='template')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', filebrowser.fields.FileBrowseField(blank=True, default=None, max_length=255, null=True, verbose_name='image')),
            ],
            options={
                'verbose_name': 'gallery',
                'ordering': ('-priority', 'name'),
                'verbose_name_plural': 'galleries',
            },
        ),
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='created')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, verbose_name='slug')),
                ('publish', models.BooleanField(choices=[(True, 'Published'), (False, 'Unpublished')], default=True, verbose_name='published')),
                ('priority', models.IntegerField(default=100, verbose_name='display priority')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', filebrowser.fields.FileBrowseField(blank=True, default=None, max_length=255, null=True, verbose_name='image')),
                ('file_type', models.CharField(choices=get_ressource_filetype_choices(), default=get_ressource_filetype_default(), max_length=55, verbose_name='file type')),
                ('file', filebrowser.fields.FileBrowseField(blank=True, default=None, max_length=255, null=True, verbose_name='file')),
                ('file_url', models.URLField(blank=True, verbose_name='file url')),
                ('tags', tagging.fields.TagField(blank=True, max_length=255, verbose_name='tags')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='porticus.Album')),
                ('related', models.ManyToManyField(blank=True, related_name='_ressource_related_+', to='porticus.Ressource')),
            ],
            options={
                'verbose_name': 'ressource',
                'ordering': ('album', 'priority'),
                'verbose_name_plural': 'ressources',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='porticus.Gallery'),
        ),
        migrations.AddField(
            model_name='album',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='porticus.Album'),
        ),
        migrations.AlterUniqueTogether(
            name='ressource',
            unique_together=set([('album', 'slug')]),
        ),
    ]
