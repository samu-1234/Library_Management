from django.shortcuts import render,redirect
from .models import Book

# Create your views here.
def index(request):
    data=Book.objects.all()
    return render(request,'base.html',{'data':data})

def showbook(request):
    data = Book.objects.all()
    return render(request, 'base.html', {'data': data})

def insertBookdetail(request):
    if request.method=='POST':
        title=request.POST['title']
        author = request.POST['author']
        publisher = request.POST['publisher']
        category = request.POST['category']
        bk=Book()
        bk.title,bk.author,bk.publisher,bk.category=title,author,publisher,category
        bk.save()
        return redirect('/show')
    return render(request,'insertbook.html')

def deletebook(request,id):
    bk=Book.objects.get(id=id)
    bk.delete()
    return redirect('/show')

def updatebook(request,id):
    bk = Book.objects.get(id=id)
    if request.method == 'POST':
            title = request.POST['title']
            author = request.POST['author']
            publisher = request.POST['publisher']
            category = request.POST['category']
            # bk = Book()
            bk.title, bk.author, bk.publisher, bk.category = title, author, publisher, category
            bk.save()
            return redirect('/show')
    return render(request, 'insertbook.html')