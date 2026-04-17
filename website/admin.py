from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Announcement, EspecificacaoTecnica, QuemSomosCard, Subsistema


@admin.register(QuemSomosCard)
class QuemSomosCardAdmin(SummernoteModelAdmin):
    # Diz ao Django qual campo vai virar o editor Word
    summernote_fields = ("descricao",)

    list_display = ("titulo", "ordem", "ativo", "atualizado_em")
    list_editable = ("ordem", "ativo")
    search_fields = ("titulo", "descricao")
    list_filter = ("ativo",)


@admin.register(Announcement)
class AnnouncementAdmin(SummernoteModelAdmin):
    # O campo message vira o editor
    summernote_fields = ("message",)

    list_display = ("message_preview", "date", "ativo")
    list_editable = ("ativo",)
    search_fields = ("message",)

    def message_preview(self, obj):
        from django.utils.html import strip_tags

        return strip_tags(obj.message)[:50] + "..."

    message_preview.short_description = "Mensagem"


@admin.register(EspecificacaoTecnica)
class EspecificacaoTecnicaAdmin(admin.ModelAdmin):
    list_display = ("rotulo", "valor", "unidade", "ordem", "ativo")
    list_editable = ("ordem", "ativo")
    search_fields = ("rotulo",)
    list_filter = ("ativo",)


@admin.register(Subsistema)
class SubsistemaAdmin(SummernoteModelAdmin):
    summernote_fields = ("conteudo_pagina",)

    # Preenche a URL automaticamente enquanto o redator digita o nome
    prepopulated_fields = {"slug": ("nome",)}

    list_display = ("nome", "ordem", "ativo")
    list_editable = ("ordem", "ativo")

    # A mágica da organização visual no painel Admin:
    fieldsets = (
        ("Configurações Básicas", {"fields": ("nome", "slug", "ativo", "ordem")}),
        (
            "Informações do Card (Página Sobre)",
            {
                "fields": ("resumo_card", "icone"),
                "description": "Estes dados aparecem nos blocos pequenos da listagem geral.",
            },
        ),
        (
            "Página Exclusiva do Subsistema",
            {
                "fields": ("conteudo_pagina",),
                "description": "Este é o conteúdo rico (com imagens e negritos) que aparece quando o usuário clica no card.",
            },
        ),
    )
