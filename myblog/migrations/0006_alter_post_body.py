# Generated by Django 5.0.7 on 2024-08-23 09:58

import django.utils.timezone
import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_alter_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
