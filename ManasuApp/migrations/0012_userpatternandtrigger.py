# Generated by Django 5.0.7 on 2024-08-03 08:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManasuApp', '0011_activity_suggested_by_ai_goal_suggested_by_ai'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPatternAndTrigger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('severity', models.PositiveSmallIntegerField(blank=True, help_text='Rate the severity (1 to 10)', null=True)),
                ('identified_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patterns_and_triggers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
