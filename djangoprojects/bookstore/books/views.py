from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Auther
from .models import Book

# Create your views here.

def index(request):
    return HttpResponse("Anasayfa")
def authors(request):
    context = {
        'authors_list' :  Auther.objects.all()
    }
    return render(request,'author.html', context)
def books(request):
    context ={
        'author_book' : Book.objects.all()
    }
    return render(request,'books.html',context)
def authorDetails(request,authorid):
    context = {
        'author_detail': Auther.objects.get()
    }
    
    return render(request,'AuthorDetail.html',context)

