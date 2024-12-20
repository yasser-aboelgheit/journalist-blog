# Generated by Django 3.2.16 on 2023-05-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0005_rename_episode_title_podcast_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='number_of_visits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='podcast',
            name='source_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
