# Generated by Django 3.2.16 on 2023-10-15 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0008_remove_podcast_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcast',
            name='youtube_link',
        ),
        migrations.AddField(
            model_name='podcast',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
