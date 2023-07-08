from django.shortcuts import render
from perfil.models import Categoria
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
def definir_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'definir_planejamento.html', {'categorias': categorias})

@csrf_exempt
def update_valor_categoria(request, id):
    try:
      #TODO: Tratar quando clicar em salvar sem ter alterado o valor, pois o mesmo retorna como decimal e está ocorrendo erro.      
      novo_valor = json.load(request)['novo_valor']      
      categoria = Categoria.objects.get(id=id)
      categoria.valor_planejamento = novo_valor
      categoria.save()
      return JsonResponse({'status': 'Sucesso'})
    except:
      return JsonResponse({'status': 'Erro'})