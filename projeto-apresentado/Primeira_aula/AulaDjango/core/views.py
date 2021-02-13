from django.shortcuts import render

# Create your views here.
def index(request): # Função da requisição
    return render(request, 'index.html')

def app(request):
    return render(request, 'index.html')