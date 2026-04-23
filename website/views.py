import json

from django.shortcuts import get_object_or_404, render

from .models import Announcement, EspecificacaoTecnica, QuemSomosCard, Subsistema


def index(request):
    # Procura os itens no banco de dados
    cards_quem_somos = QuemSomosCard.objects.filter(ativo=True)
    announcements = Announcement.objects.filter(ativo=True)
    specs_tecnicas = EspecificacaoTecnica.objects.filter(ativo=True)

    # Monta um contexto único e organizado
    context = {
        "about_items": cards_quem_somos,
        "announcements": announcements,
        "specs": specs_tecnicas,
    }

    return render(request, "website/pages/home.html", context)


def about(request):
    """View para a listagem dos cards"""
    # PERFORMANCE: .only() diz ao banco de dados para NÃO carregar o 'conteudo_pagina'
    # que é pesado, já que não vamos usá-lo na listagem dos cards.
    subsistemas = Subsistema.objects.filter(ativo=True).only(
        "nome", "slug", "resumo_card", "icone"
    )

    context = {
        "subsistemas": subsistemas,
    }
    return render(request, "website/pages/about.html", context)


def subsystem_detail(request, slug):
    """View para a página específica do subsistema"""
    # get_object_or_404 tenta achar o item, se a URL estiver errada, retorna erro 404 seguro
    subsistema = get_object_or_404(Subsistema, slug=slug, ativo=True)

    context = {
        "subsistema": subsistema,
    }
    return render(request, "website/pages/subsystem_detail.html", context)
