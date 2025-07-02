from django.shortcuts import render
from django.http import JsonResponse
from .models import Cidade

def carrega_cidades(request):
    estado_id = request.GET.get('estado')
    cidades = Cidade.objects.filter(estado_id=estado_id).values('id', 'nome')
    return JsonResponse(list(cidades), safe=False)
