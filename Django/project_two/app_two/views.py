from django.shortcuts import render


def index(request):
    index_dict = {'index_key': 'My Second App'}
    return render(request, 'app_two/index.html', context=index_dict)


def help_page(request):
    help_dict = {'help_key': 'this is from views.py'}
    return render(request, 'app_two/help_page.html', context=help_dict)
