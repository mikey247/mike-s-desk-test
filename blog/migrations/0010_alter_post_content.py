# Generated by Django 4.0.1 on 2022-01-30 22:41

import django.core.validators
from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Content',
            field=tinymce.models.HTMLField(validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]