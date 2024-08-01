# Generated by Django 5.0.7 on 2024-08-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManasuApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='additional_info',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
