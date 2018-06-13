from django.shortcuts import render,redirect
from .models import Book
from django.http import HttpResponse

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request,'list.html',{'books':books})

def isbn(request,isbn):
    books = Book.objects.filter(isbn=isbn)
    return render(request,'list.html',{'books':books})

def delete(request,id):
    book = Book.objects.filter(id = id)
    book[0].delete()
    return render(request,'list.html',{'id':id,'book':book})

def update(request,id):
    if request.method == 'POST':
        name  = request.POST['name']
        isbn = request.POST['isbn']
        author  = request.POST['author']
        book = Book.objects.get(id = id)
        book.name = name
        book.isbn = isbn
        book.author = author
        book.save()
        return redirect('/')
    return render(request,'book_update.html',{'id':id})

def add(request):
    if request.method == 'POST':
        name  = request.POST['name']
        isbn = request.POST['isbn']
        author  = request.POST['author']
        book = Book(name = name,author = author,isbn = isbn)
        book.save()
        return redirect('/')
    return render(request,'book_add.html')