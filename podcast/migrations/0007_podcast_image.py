# Generated by Django 3.2.16 on 2023-10-15 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0006_auto_20230514_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/blogs'),
        ),
    ]