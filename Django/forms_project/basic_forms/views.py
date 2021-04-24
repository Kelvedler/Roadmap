from django.shortcuts import render
from basic_forms import forms


def index(request):
    return render(request, 'basic_forms/index.html')


def form_name_view(request):
    form = {'form': forms.FormName()}
    return render(request, 'basic_forms/form_page.html', context=form)
