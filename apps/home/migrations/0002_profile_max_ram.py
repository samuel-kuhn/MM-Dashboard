# Generated by Django 3.2.16 on 2024-01-10 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='max_ram',
            field=models.IntegerField(blank=True, default=5),
        ),
    ]
