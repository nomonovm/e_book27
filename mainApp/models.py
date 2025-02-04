from django.db import models


class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    haqida = models.CharField(max_length=155)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = 'Bolimlar'


class Muallif(models.Model):
    ism = models.CharField(max_length=120)
    tirik = models.BooleanField(default=False)
    davlat = models.CharField(max_length=133)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = 'Mualliflar'


class Kitob(models.Model):
    nom = models.CharField(max_length=111)
    muallif = models.ForeignKey(Muallif, on_delete=models.SET_NULL, null=True)
    yili = models.DateField()
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)
    file = models.FileField()

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = 'Kitoblar'
