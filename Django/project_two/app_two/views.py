from django.shortcuts import render
from app_two import forms


def index(request):
    index_dict = {'index_key': 'My Second App'}
    return render(request, 'app_two/index.html', context=index_dict)


def help_page(request):
    help_dict = {'help_key': 'this is from views.py'}
    return render(request, 'app_two/help_page.html', context=help_dict)


def users(request):
    form = forms.UserInput()
    if request.method == 'POST':
        form = forms.UserInput(request.POST)

        if form.is_valid():
            form.save(commit=True)

    return render(request, 'app_two/users.html', context={'form': form})
