# Generated by Django 2.2.6 on 2019-11-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dl', '0002_teacher_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grades',
            name='grade',
            field=models.IntegerField(default=0),
        ),
    ]
