from django.shortcuts import render
from first_app.models import Topic, Webpage, AccessField


def index(request):
    webpages_list = AccessField.objects.order_by('date')
    date_dict = {'access_fields': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)
