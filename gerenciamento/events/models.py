from django.db import models

class Evento(models.Model):
    TIPOS_EVENTO = [
        ('show', 'Show'),
        ('teatro', 'Teatro'),
        ('orquestra', 'Orquestra'),
        ('musical', 'Musical'),
        ('humor','Humor')
    ]

    titulo =models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPOS_EVENTO)
    dataInicial =models.DateTimeField()
    dataFinal = models.DateTimeField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gratuito = models.BooleanField(default=False)
    local = models.CharField(max_length=200)
    horario = models.TimeField()
    cidade =models.CharField(max_length=100)
    vagas = models.PositiveBigIntegerField(null= True, blank=True)
    
    def __str__(self):
        return self.titulo