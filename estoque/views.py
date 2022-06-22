from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from estoque.forms import VendaForm
from estoque.models import Venda

def list_venda(request):
    vendas = Venda.objects.all()
    print("1")
    return render(request, 'venda.html', {'vendas': vendas})


def create_venda(request):
    form = VendaForm(request.POST or None)
    print("2")
    if form.is_valid():
        print("3")
        form.save()
        return redirect('list_venda')

    return render(request, 'venda-form.html', {'form': form})


def update_venda(request, id):
    vendas = Venda.objects.get(id=id)
    form = VendaForm(request.POST or None, instance=vendas)

    if form.is_valid():
        form.save()
        return redirect('list_venda')

    return render(request, 'venda-form.html', {'form': form, 'venda': vendas})


def delete_venda(request, id):
    venda = Venda.objects.get(id=id)

    if request.method == 'POST':
        venda.delete()
        return redirect('list_venda')

    return render(request, 'venda-delete-confirm.html', {'venda': venda})

