# Generated by Django 5.0.4 on 2024-08-16 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='status',
        ),
    ]