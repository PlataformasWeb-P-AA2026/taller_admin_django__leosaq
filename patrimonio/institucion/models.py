from django.db import models


class Museo(models.Model):
    nombre = models.CharField("Nombre del museo", max_length=100, unique=True)
    ciudad = models.CharField("Ciudad del museo", max_length=100)
    anio_fundacion = models.IntegerField("Año de fundación")

    def __str__(self):
        return "%s - ciudad: %s - año de fundación: %d" % (
            self.nombre,
            self.ciudad,
            self.anio_fundacion
        )

    def obtener_costo_total_exhibiciones(self):
        total = 0
        for guia in self.gui_museo_set.all():
            for exhibicion in guia.exhibicion_set.all():
                total = total + exhibicion.costo_produccion
        return total

    def obtener_guia_mas_experiencia(self):
        guia = self.gui_museo_set.order_by('-anios_experiencia_guia').first()
        if guia:
            return guia.nombre_completo
        return "Sin guías"


class GuiaMuseo(models.Model):
    nombre_completo = models.CharField("Nombre completo del guía", max_length=150)
    anios_experiencia_guia = models.IntegerField("Años de experiencia como guía")
    idiomas_hablados = models.CharField("Idiomas hablados", max_length=200)

    museo = models.ForeignKey(Museo, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - experiencia: %d años - idiomas: %s - museo: %s" % (
            self.nombre_completo,
            self.anios_experiencia_guia,
            self.idiomas_hablados,
            self.museo.nombre
        )


class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField("Título de exhibición", max_length=150)
    duracion_meses = models.IntegerField("Duración en meses")
    costo_produccion = models.DecimalField("Costo de producción", max_digits=10, decimal_places=2)
    tematica = models.CharField("Temática", max_length=100)

    guia = models.ForeignKey(GuiaMuseo, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - duración: %d meses - costo: %s - temática: %s - guía: %s" % (
            self.titulo_exhibicion,
            self.duracion_meses,
            self.costo_produccion,
            self.tematica,
            self.guia.nombre_completo
        )