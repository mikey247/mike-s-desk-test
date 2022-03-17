# Generated by Django 4.0.1 on 2022-03-17 11:44

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Content',
            field=ckeditor_uploader.fields.RichTextUploadingField(validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
