# Generated by Django 3.2.16 on 2023-05-07 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0001_initial'),
        ('investigations', '0004_auto_20230507_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigation',
            name='published_on',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='publisher.publisher'),
        ),
    ]