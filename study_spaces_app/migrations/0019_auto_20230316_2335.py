# Generated by Django 2.2.28 on 2023-03-16 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_spaces_app', '0018_auto_20230316_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='UserProfile',
            new_name='userProfile',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='UserProfile',
            new_name='userProfile',
        ),
    ]
