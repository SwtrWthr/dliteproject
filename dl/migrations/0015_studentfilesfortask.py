# Generated by Django 2.2.7 on 2019-12-09 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dl', '0014_gradesfortask'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFilesForTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dl.Student')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dl.Task')),
            ],
            options={
                'db_table': 'students_files',
            },
        ),
    ]