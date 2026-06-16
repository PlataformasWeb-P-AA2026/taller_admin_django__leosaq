from django.contrib import admin

from institucion.models import Museo, GuiaMuseo, Exhibicion


class MuseoAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'ciudad',
        'anio_fundacion',
        'obtener_costo_total_exhibiciones',
        'obtener_guia_mas_experiencia'
    )

    search_fields = ('nombre', 'ciudad')


admin.site.register(Museo, MuseoAdmin)


class GuiaMuseoAdmin(admin.ModelAdmin):

    list_display = (
        'nombre_completo',
        'anios_experiencia_guia',
        'idiomas_hablados',
        'get_museo'
    )

    raw_id_fields = ('museo',)

    def get_museo(self, obj):
        return obj.museo.nombre


admin.site.register(GuiaMuseo, GuiaMuseoAdmin)


class ExhibicionAdmin(admin.ModelAdmin):

    list_display = (
        'titulo_exhibicion',
        'duracion_meses',
        'costo_produccion',
        'tematica',
        'get_guia'
    )

    raw_id_fields = ('guia',)

    def get_guia(self, obj):
        return obj.guia.nombre_completo


admin.site.register(Exhibicion, ExhibicionAdmin)