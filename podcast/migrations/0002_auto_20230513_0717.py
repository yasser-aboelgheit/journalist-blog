# Generated by Django 3.2.16 on 2023-05-13 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_tags'),
        ('podcast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='episode_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='podcast',
            name='episode_title',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='podcast',
            name='published_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='snippet',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='podcast',
            name='tag',
            field=models.ManyToManyField(blank=True, to='home.Tags'),
        ),
        migrations.AddField(
            model_name='podcast',
            name='video',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='podcast',
            name='youtube_link',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
