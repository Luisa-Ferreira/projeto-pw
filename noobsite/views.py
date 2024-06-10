from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def intro(request):
    return HttpResponse('Hello host')

def Hello(request,nome):
    return HttpResponse(f'Hello {nome}')