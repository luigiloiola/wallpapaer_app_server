# Generated by Django 4.2.9 on 2024-02-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='currentWallpaper',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]