# Generated by Django 2.2.1 on 2019-06-27 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20190627_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='ponderacion',
            field=models.IntegerField(default=0),
        ),
    ]
