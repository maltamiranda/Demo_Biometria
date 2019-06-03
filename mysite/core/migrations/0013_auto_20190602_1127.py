# Generated by Django 2.2.1 on 2019-06-02 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_agente'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='agente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='agente', to='core.Agente'),
        ),
        migrations.AddField(
            model_name='audio',
            name='campaña',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='campaña_audio', to='core.Campaña'),
        ),
        migrations.AddField(
            model_name='audio',
            name='idInteraccion',
            field=models.CharField(default=None, max_length=60, unique=True),
        ),
        migrations.AddField(
            model_name='audio',
            name='inicio',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=models.FileField(default=None, upload_to='audios/files/'),
        ),
    ]