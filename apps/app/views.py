from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from .models.user import User
from json import JSONDecoder, JSONEncoder
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers


# Create your views here.

@csrf_protect
def index(request):
    context = {}
    return render(request, 'app/index.html', context)


@require_http_methods(['GET'])
def saludo(request):
    lista = User.objects.get(pk=1)

    print(lista)
    data = {
        "id": lista.id,
        "name": lista.name,
        "email": lista.email,
        "password": lista.password,
    }

    # data = serializers.serialize('json', lista)
    return JsonResponse(data)
    # return JsonResponse(json.dumps(lista.name), safe=False)


@require_http_methods(['POST'])
def login(request):
    username = request.POST.get('email')
    password = request.POST.get('password')
    stayloggedin = request.POST.get('stayloggedin')
    if stayloggedin == "true":
        pass
    else:
        request.session.set_expiry(0)

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse('fine')
        else:
            return HttpResponse('inactive')
    else:
        return HttpResponse('bad')
