# Generated by Django 3.0.4 on 2020-03-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('wyniki', '0002_auto_20200321_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='more_better',
            field=models.BooleanField(null=True),
        ),
    ]
