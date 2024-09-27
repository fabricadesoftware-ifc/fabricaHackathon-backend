# Generated by Django 5.0.4 on 2024-09-27 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0004_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ['photo_base64'], 'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
        migrations.RenameField(
            model_name='images',
            old_name='edition_photo_base64',
            new_name='photo_base64',
        ),
    ]