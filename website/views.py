from django.shortcuts import render




def index(request):
    data = {}
    return render(request, 'index.html', data)
