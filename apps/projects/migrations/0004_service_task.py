# Generated by Django 3.0.8 on 2020-08-07 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0012_periodictask_expire_seconds'),
        ('projects', '0003_service_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_celery_beat.PeriodicTask'),
        ),
    ]
