# Generated by Django 5.1.1 on 2024-10-22 18:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
        ('teachers', '0006_alter_assignment_uploaded_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='platform',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administration.platform'),
        ),
    ]