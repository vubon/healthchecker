# Generated by Django 3.2.12 on 2022-04-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_auto_20220414_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
