# Generated by Django 5.1.5 on 2025-03-01 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='/profiles/default_profile_picture.jpg', null=True, upload_to='profiles/'),
        ),
    ]
