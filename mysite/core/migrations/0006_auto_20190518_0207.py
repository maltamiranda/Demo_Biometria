# Generated by Django 2.2.1 on 2019-05-18 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190517_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='canal_1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='canal_2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='nombre',
            field=models.TextField(),
        ),
    ]