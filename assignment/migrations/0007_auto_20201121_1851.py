# Generated by Django 3.1.2 on 2020-11-21 18:51

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0006_auto_20201121_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentquestion',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='answer_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
