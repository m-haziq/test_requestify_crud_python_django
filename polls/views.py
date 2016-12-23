from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import requests

import bs4
from .models import Sampletable

def index(request):
    list_contacts = Sampletable.objects.order_by('phone')[:5]
    template = loader.get_template('polls/index.html')
    context = {
            'list_contacts':list_contacts,
        }
    
    return HttpResponse(template.render(context, request))

@csrf_exempt
def ajax_func(request):
    
    boxValue = request.POST.get('value')
    boxValueArray = boxValue.split(',')
    urlArray = []
    titleArray = []
    for q in boxValueArray:
        temp = 'https://www.'+q
        res = requests.get(temp)
        mySoup = bs4.BeautifulSoup(res.text, 'html.parser')
        urlArray.append(temp)
        titleArray.append(mySoup.title.text)

    response = {}
    response['urlArray'] = urlArray
    response['titleArray'] = titleArray
    
    return HttpResponse(json.dumps(response))

@csrf_exempt
def delete_func(request):
    sid = request.POST.get('id')
    q = Sampletable.objects.get(pk=sid)
    q.delete()
    print sid
    response = {}
    response['sid'] = sid
    return HttpResponse(json.dumps(response))

@csrf_exempt
def update_func(request):
    sid = request.POST.get('id')
    url = request.POST.get('url')
    name = request.POST.get('name')

    q = Sampletable.objects.get(pk=sid)
    q.name = url
    q.phone = name
    q.save()
    response = {}
    response['sid'] = sid
    return HttpResponse(json.dumps(response))
 
def detail(request):

    url_value= request.POST.get('url')
    urls= url_value.split(',')

    for q in urls:
        temp = 'https://www.'+q
        res = requests.get(temp)
        mysoup = bs4.BeautifulSoup(res.text, 'html.parser')
        q = Sampletable(name=temp , phone=mysoup.title.text)
        q.save()
    
    return render(request, 'polls/detail.html', {'url': len(urls) })

def database(request):
    q = Sampletable.objects.all()
    return render(request, 'polls/database.html', {'data':q})

def url_page(request):
    return render(request, 'polls/url_page.html')
    
def results(request, sampletable_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % sampletable_id)
def vote(request, sampletable_id):
    return HttpResponse("You are voting on %s" % sampletable_id)
