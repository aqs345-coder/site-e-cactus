from django.shortcuts import render
import json

def index(request):
    announcements = [
        {"message": "Inscrições abertas para a temporada 2026!", "date": "15/04/2026"},
        {"message": "Novo projeto de suspensão desenvolvido", "date": "10/04/2026"},
        {"message": "Parceria com empresa de baterias confirmada", "date": "05/04/2026"},
    ]
    return render(request, 'core/home.html', {"announcements": announcements})
