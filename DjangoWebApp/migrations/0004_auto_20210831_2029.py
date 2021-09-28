# Generated by Django 3.2.6 on 2021-08-31 18:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoWebApp', '0003_bug_severity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bug',
            old_name='body',
            new_name='solution',
        ),
        migrations.RemoveField(
            model_name='bug',
            name='severity',
        ),
        migrations.AddField(
            model_name='bug',
            name='priority',
            field=models.CharField(choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bug',
            name='state',
            field=models.CharField(choices=[('Resuelto', 'Resuelto'), ('En proceso', 'En Proceso'), ('Planeado', 'Planeado')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]