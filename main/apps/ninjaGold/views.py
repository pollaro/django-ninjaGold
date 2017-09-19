from django.shortcuts import render, redirect
import random

def index(request):
    print 'index'
    if 'money' not in request.session:
        request.session['money'] = 0
        request.session['cash'] = 0
        request.session['location'] = 'Farm'
        request.session['color'] = 'Green'
        request.session['oldtext'] = ''
    return render(request,'ninjaGold/index.html')

def process(request):
    print 'process'
    rand = random.random()
    print request.POST['building']
    if request.POST['building'] == 'Farm':
        cash = round(rand*(10)+10)
        request.session['location'] = 'Farm'
    elif request.POST['building'] == 'Cave':
        cash = round(rand*(5)+5)
        request.session['location'] = 'Cave'
    elif request.POST['building'] == 'House':
        cash = round(rand*(3)+2)
        request.session['location'] = 'House'
    elif request.POST['building'] == 'Casino':
        cash = round(rand*(100)-50)
        if cash < 0:
            request.session['color'] = 'Red'
        else:
            request.session['color'] = 'Green'
        request.session['location'] = 'Casino'
    request.session['money'] += cash
    request.session['money'] = int(request.session['money'])
    request.session['cash'] = int(cash)
    return redirect('/')
