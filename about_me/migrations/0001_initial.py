# Generated by Django 3.2.16 on 2023-12-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wide_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('bio', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]