# Generated by Django 3.2.16 on 2023-05-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigations', '0005_investigation_published_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigation',
            name='number_of_visits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='investigation',
            name='source_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
