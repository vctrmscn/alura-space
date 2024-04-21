# Register your models here.
from django.contrib import admin

from galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = (
        "id",
        "publicada",
        "categoria",
        "nome",
        "foto",
        "legenda",
        "descricao",
        "data_fotografia",
    )
    list_display_links = (
        "id",
        "nome",
    )
    search_fields = ("nome",)
    list_filter = (
        "publicada",
        "categoria",
    )
    list_editable = ("publicada",)
    list_per_page = 10


admin.site.register(Fotografia, ListandoFotografias)
