# Generated by Django 4.2.13 on 2024-07-29 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeriaCiencias', '0004_articulo_link_proyecto_link_seccion_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='link',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='artimagen',
            name='imagen',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='link',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='seccion',
            name='imagen',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='seccion',
            name='link',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='seccion',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
