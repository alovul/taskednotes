# Generated by Django 4.2.3 on 2024-02-21 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='img/profile_pictures/'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
