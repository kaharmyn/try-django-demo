# Generated by Django 4.2.3 on 2023-09-10 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_timestamp_article_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='update',
            new_name='updated',
        ),
    ]
