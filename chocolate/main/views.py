from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Types
from .forms import TypesForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    types = Types.objects.order_by('id')
    """[:3]"""
    return render(request, 'main/about.html', {'title': 'Виды шоколада', 'types': types})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TypesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
        else:
            error = 'Форма не верна'

    form = TypesForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def black(request):
    return render(request, 'main/black.html')


def milk(request):
    return render(request, 'main/milk.html')


def white(request):
    return render(request, 'main/white.html')


class TypesView(View):
    def get(self, request):
        types = Types.objects.all()
        return render(request, 'main/types_list.html', {'types_list': types})