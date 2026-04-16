import json

from django.shortcuts import render

from .models import Announcement, EspecificacaoTecnica, QuemSomosCard


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

    return render(request, "website/home.html", context)
