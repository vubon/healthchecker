# Generated by Django 3.0.8 on 2020-08-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
        migrations.AddField(
            model_name='service',
            name='interval',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
