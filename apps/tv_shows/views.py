from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import Show

def index(request):
    print('request method is running')
    return render(request, 'tv_shows/index.html')

def addshow(request):
    print('addshow method is running')
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
        messages.success(request, "Title successfully added!")
        return redirect (f'/shows/{show.id}')

def showdetails(request, id):
    print('showdetails method is running')
    context ={
        'show': Show.objects.get(id=id),
    }
    return render(request, 'tv_shows/shows.html', context)

def destroy(request, id):
    print('destroy method is running')
    c=Show.objects.get(id=id)
    c.delete()
    return redirect('/shows')

def mainshowpage(request):
    print('mainshowpage method is running')
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'tv_shows/allshows.html', context)

def editshow(request, id):
    print('editshow method is running')
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, 'tv_shows/editshow.html', context)

def updateshow(request, id):
    print('updateshow method is running')
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    else:
        show = Show.objects.get(id=id)
        c=Show.objects.get(id=id)
        c.title=request.POST['title']
        c.network=request.POST['network']
        c.release_date=request.POST['release_date']
        c.description=request.POST['description']
        c.save()
        return redirect(f'/shows/{id}')




# Create your views here.
