# Generated by Django 3.2.16 on 2023-05-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0003_podcast_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='episode_title',
            field=models.CharField(max_length=255),
        ),
    ]
