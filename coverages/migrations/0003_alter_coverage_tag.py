# Generated by Django 3.2.16 on 2022-12-16 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_tags'),
        ('coverages', '0002_auto_20221215_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverage',
            name='tag',
            field=models.ManyToManyField(blank=True, to='home.Tags'),
        ),
    ]
