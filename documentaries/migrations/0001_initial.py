# Generated by Django 3.2.16 on 2023-05-04 21:08

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/investigations')),
                ('snippet', models.TextField(blank=True, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('published_at', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.ManyToManyField(blank=True, to='home.Tags')),
            ],
            options={
                'ordering': ('published_at',),
            },
        ),
    ]
