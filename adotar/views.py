from django.shortcuts import render
from django.http import HttpResponse
from divulgar.models import Pet, Raca

def listar_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(status="P")
        racas = Raca.objects.all()

        cidade = request.GET.get('cidade')
        raca_filter = request.GET.get('raca')

        if cidade:
            pets = pets.filter(cidade__icontains=cidade)    #isso serve para quando precisa pesquisar algo, mas por caracteres

        if raca_filter:
            pets = pets.filter(raca__id=raca_filter)       #filtrar pelo ID do pet
            raca_filter = Raca.objects.get(id=raca_filter)

        return render(request, 'listar_pets.html', {'pets': pets, 'racas': racas, 'cidade':cidade, 'raca_filter':raca_filter})