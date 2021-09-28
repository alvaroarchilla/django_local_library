# Generated by Django 3.2.6 on 2021-09-04 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_categorias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='name',
            field=models.CharField(choices=[('Electrónica', 'Electrónica'), ('Desarrollo Web', 'Desarrollo Web'), ('DataScience & IA', 'DataScience & IA'), ('Impresión 3D', 'Impresión 3D'), ('Otros Posts', 'Otros Posts')], max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='categorias',
            field=models.ManyToManyField(to='blog.Categoria'),
        ),
    ]