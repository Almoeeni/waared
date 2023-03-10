# Generated by Django 4.1.7 on 2023-03-04 10:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_studentname_student_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='studentName',
            field=models.CharField(default=1, max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s]*$|^[\\u0621-\\u064A\\s]*$', 'Only English and Arabic characters are allowed.')]),
            preserve_default=False,
        ),
    ]
