from django.db import models

class Fiscal(models.Model):
    nome = models.CharField(max_length=30, blank=False)
    regional = models.IntegerField(blank=False)
    email = models.EmailField(max_length=100, default='seuemail@gmail.com', blank=False)

    def __str__(self):
        return self.nome

    def __str__(self):
        return self.regional

    class Meta:
        verbose_name_plural = "Fiscal"

class Hora_extra(models.Model):
    nome = models.CharField(max_length=30, blank=False)
    data = models.DateField()
    horario = (models.IntegerField(blank=False))
    descricao = models.CharField(max_length=30,blank=True)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Hora Extra"

class Dia_da_semana(models.Model):
    nome = models.ForeignKey( Fiscal, on_delete=models.CASCADE)
    fiscal_responsavel= models.ForeignKey(Fiscal, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.Dia_da_semana.horario} - {self.Dia_da_semana.fiscal_responsavel}"

    class Meta:
        verbose_name_plural = "Dia_da_semana"


class Administrador(models.Model):
    nome = models.CharField(blank=False)
    senha = models.FloatField(blank=False)

    def __str__(self):
        return f"{self.nome},{self.senha}"

    class Meta:
        verbose_name_plural = "Administradores"