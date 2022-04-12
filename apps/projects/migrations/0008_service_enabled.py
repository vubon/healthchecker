# Generated by Django 3.2.12 on 2022-04-12 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_service_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='enabled',
            field=models.BooleanField(default=True, help_text='Set to False to disable the schedule', verbose_name='Enabled'),
        ),
    ]
