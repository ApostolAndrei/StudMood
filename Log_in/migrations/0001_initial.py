# Generated by Django 3.0.6 on 2020-06-11 23:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materials_title', models.CharField(max_length=200)),
                ('materials_content', models.TextField()),
                ('materials_published', models.DateTimeField(default=datetime.datetime(2020, 6, 12, 2, 50, 31, 489826), verbose_name='date published')),
            ],
        ),
    ]
