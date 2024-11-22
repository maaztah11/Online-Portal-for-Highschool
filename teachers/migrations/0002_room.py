# Generated by Django 5.1.1 on 2024-10-05 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=10)),
                ('room_code', models.CharField(max_length=5)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teachers.teacherprofile')),
            ],
        ),
    ]