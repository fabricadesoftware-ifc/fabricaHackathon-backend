# Generated by Django 5.0.4 on 2024-10-10 21:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0002_alter_edition_involved_classes'),
        ('user', '0002_studentprofile_class_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='leader', to='user.studentprofile'),
        ),
        migrations.AlterField(
            model_name='team',
            name='students',
            field=models.ManyToManyField(related_name='students', to='user.studentprofile'),
        ),
    ]