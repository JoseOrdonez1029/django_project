# Generated by Django 4.1.7 on 2023-05-05 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apipaciente', '0003_alter_paciente_apellidopac_alter_paciente_nombrepac'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='apellidoPac',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='edadPac',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='nombrePac',
        ),
    ]
