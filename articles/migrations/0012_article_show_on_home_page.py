# Generated by Django 3.2.16 on 2023-12-02 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_alter_article_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='show_on_home_page',
            field=models.BooleanField(default=False),
        ),
    ]