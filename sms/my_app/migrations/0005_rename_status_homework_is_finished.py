# Generated by Django 5.0.3 on 2024-03-15 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_homework'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homework',
            old_name='status',
            new_name='is_finished',
        ),
    ]