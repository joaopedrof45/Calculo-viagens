from django.db import models

class Calculos(models.Model):
    defensorbool= models.BooleanField('defensor')
    numero_protocolo= models.CharField('Numero Protocolo',primary_key=True ,max_length=500)
    dias_utei=models.IntegerField('Dias úteis')
    data_inical=models.DateTimeField('Data Inicial')
    data_final=models.DateTimeField('Data Final')
    valor_passagem = models.IntegerField('Valor Passagem')
    valor_translado= models.IntegerField('Valor Translado')
    cargo = models.CharField('Cargo',max_length=50)
    estado= models.CharField('Estado',max_length=50)
    cidade= models.CharField('Cidade',max_length=50)
    created_at = models.DateTimeField('Criado em ' , auto_now=True)
    update_at = models.DateTimeField('Atualizado em ' , auto_now=True)
    


    def __str__(self):
        return self.numero_protocolo

    class Meta:
        verbose_name='Calculo'
        verbose_name_plural='Calculos'
        ordering=['numero_protocolo']
