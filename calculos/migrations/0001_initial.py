# Generated by Django 3.2.7 on 2022-01-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defensorbool', models.IntegerField(verbose_name='defensor')),
                ('numero_protocolo', models.IntegerField(verbose_name='Numero Protocolo')),
                ('dias_utei', models.IntegerField(verbose_name='Dias úteis')),
                ('data_inical', models.DateTimeField(verbose_name='Data Inicial')),
                ('data_final', models.DateTimeField(verbose_name='Data Final')),
                ('valor_passagem', models.IntegerField(verbose_name='Valor Passagem')),
                ('valor_translado', models.IntegerField(verbose_name='Valor Translado')),
                ('cargo', models.CharField(max_length=50, verbose_name='Cargo')),
                ('estado', models.CharField(max_length=50, verbose_name='Estado')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Criado em ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em ')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['numero_protocolo'],
            },
        ),
    ]
