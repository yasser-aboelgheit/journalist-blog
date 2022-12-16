# Generated by Django 3.2.16 on 2022-12-15 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('published_at',)},
        ),
        migrations.AddField(
            model_name='article',
            name='published_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
