from django.shortcuts import render

mhs_name = 'Rafif Iqbal Shaputra'

def index(request):
    response ={'name': mhs_name}
    return render(request, 'index_lab1.html', response)
