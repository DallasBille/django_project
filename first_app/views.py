from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
# This is where you have functions to handle requests and return responses.
# Create your views here.

# You must map this to your urls.py file to get anything to show up.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    my_dictionary = {'insert_me': "From first_app, index.html"}
    return render(request, 'first_app/index.html',context=date_dict)
