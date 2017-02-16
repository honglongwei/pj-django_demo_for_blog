from django.shortcuts import render_to_response
#from django.http import HttpResponse
from models import Blog_News


def index(request):
    nrong = Blog_News.objects.all().order_by('-id')
    return render_to_response('blog01/index.html', {'nrong':nrong})


def acticles(request, title_id):
    nbl = Blog_News.objects.get(id=title_id)
    return render_to_response('blog01/acticles.html', {'nbl':nbl})


def edit_page(request, title_id):
    if str(title_id) == '0':
        return render_to_response('blog01/edit_page.html')
    nrong = Blog_News.objects.get(id=title_id)
    return render_to_response('blog01/edit_page.html', {'nrong':nrong})


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    title_id = request.POST.get('title_id', '0')
    if title_id == '0':
        Blog_News.objects.create(title=title, content=content)
        nrong = Blog_News.objects.all().order_by('-id')
        return render_to_response('blog01/index.html', {'nrong':nrong})
    acticle = Blog_News.objects.get(id=title_id)
    acticle.title = title
    acticle.content = content
    acticle.save()
    nrong = Blog_News.objects.all().order_by('-id')
    return render_to_response('blog01/index.html', {'nrong':nrong})
    
