# Generated by Django 3.2.16 on 2023-12-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0002_auto_20231203_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutmepage',
            old_name='wide_image',
            new_name='main_image_big',
        ),
        migrations.AddField(
            model_name='aboutmepage',
            name='main_image_small',
            field=models.ImageField(blank=True, null=True, upload_to='images/about'),
        ),
    ]
