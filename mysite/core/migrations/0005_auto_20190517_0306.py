# Generated by Django 2.2.1 on 2019-05-17 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_palabras_porcentaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palabras',
            name='fk_funcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcion', to='core.Funcion'),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='fk_audio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audio', to='core.Audio'),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='fk_funcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcion_reporte', to='core.Funcion'),
        ),
    ]