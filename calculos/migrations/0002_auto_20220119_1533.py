# Generated by Django 3.2.7 on 2022-01-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calculos',
            options={'ordering': ['numero_protocolo'], 'verbose_name': 'Calculo', 'verbose_name_plural': 'Calculos'},
        ),
        migrations.RemoveField(
            model_name='calculos',
            name='id',
        ),
        migrations.AlterField(
            model_name='calculos',
            name='numero_protocolo',
            field=models.CharField(max_length=500, primary_key=True, serialize=False, verbose_name='Numero Protocolo'),
        ),
    ]