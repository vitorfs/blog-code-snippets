# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'core/home.html')

def filtrar_cidade(request):
  mg = [[1, u'Juiz de Fora'], [2, u'Belo Horizonte'], [3, u'Ouro Preto']]
  rj = [[4, u'Rio de Janeiro'], [5, u'Cabo Frio'], [6, u'Búzios']]
  sp = [[7, u'São Paulo'], [8, u'Barueri'], [9, u'Campinas']]
  
  estado = request.GET.get('estado')

  html = u'<option value="">Selecione...</option>'

  if estado == 'MG':
    for cidade in mg:
      html = u'{0}<option value="{1}">{2}</option>'.format(html, cidade[0], cidade[1])

  elif estado == 'RJ':
    for cidade in rj:
      html = u'{0}<option value="{1}">{2}</option>'.format(html, cidade[0], cidade[1])

  elif estado == 'SP':
    for cidade in sp:
      html = u'{0}<option value="{1}">{2}</option>'.format(html, cidade[0], cidade[1])

  return HttpResponse(html)