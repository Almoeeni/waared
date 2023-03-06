# Generated by Django 4.1.7 on 2023-03-03 17:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.AutoField(primary_key=True, serialize=False)),
                ('studentNumber', models.CharField(max_length=10)),
                ('studentName', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s]*$|^[\\u0621-\\u064A\\s]*$', 'Only English and Arabic characters are allowed.')])),
                ('facultyName', models.CharField(max_length=100)),
                ('studentEmail', models.EmailField(max_length=256)),
                ('DateOfBirth', models.DateTimeField()),
            ],
        ),
    ]