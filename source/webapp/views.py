from django.shortcuts import render
from django.http import HttpResponseRedirect
from webapp.cat import Cat



def index(request):
    if Cat.name:
        return HttpResponseRedirect('/cat_stats/')

    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        if name:
            Cat.name = name
            return HttpResponseRedirect('/cat_stats/')
        return HttpResponseRedirect('/')

def cat_stats(request):
    if not Cat.name:
        return HttpResponseRedirect('/')
    if request.method == "POST":
        action = request.POST.get('action')
        Cat.action(action)
        return HttpResponseRedirect('/cat_stats/')

    return render(request, 'cat_stats.html', {'cat': Cat})