# Generated by Django 2.2.1 on 2019-07-04 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_audio_ponderacion'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reporte',
            unique_together={('fk_audio', 'fk_funcion')},
        ),
        migrations.RemoveField(
            model_name='reporte',
            name='fk_analisis',
        ),
        migrations.DeleteModel(
            name='Analisis',
        ),
    ]