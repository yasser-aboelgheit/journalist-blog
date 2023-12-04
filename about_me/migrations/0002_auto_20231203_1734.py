# Generated by Django 3.2.16 on 2023-12-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmepage',
            name='image_section_five',
            field=models.ImageField(blank=True, null=True, upload_to='images/about'),
        ),
        migrations.AddField(
            model_name='aboutmepage',
            name='image_section_four',
            field=models.ImageField(blank=True, null=True, upload_to='images/about'),
        ),
        migrations.AddField(
            model_name='aboutmepage',
            name='image_section_one',
            field=models.ImageField(blank=True, null=True, upload_to='images/about'),
        ),
        migrations.AddField(
            model_name='aboutmepage',
            name='image_section_three',
            field=models.ImageField(blank=True, null=True, upload_to='images/about'),
        ),
        migrations.AddField(
            model_name='aboutmepage',
            name='image_section_two',
            field=models.ImageField(blank=True, null=True, upload_to='images/about'),
        ),
        migrations.AlterField(
            model_name='aboutmepage',
            name='wide_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/about'),
        ),
    ]