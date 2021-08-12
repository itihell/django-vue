from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


# Create your views here.

@csrf_protect
def index(request):
    context = {

    }

    return render(request, 'app/index.html', context)


@require_http_methods(['POST'])
def saludo(request):
    context = {
        "saludo": 'Hola mundo'
    }
    return JsonResponse(context)
