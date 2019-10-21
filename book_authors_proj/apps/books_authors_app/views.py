from django.shortcuts import render, HttpResponse, redirect
from .models import Author, Book

def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, 'books_authors_app/index.html', context)

def authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, 'books_authors_app/author.html', context)

def authors_num (request, id):
    context = {
        "author": Author.objects.get(id=id),
        "all_books": Book.objects.all()
    }
    return render(request, 'books_authors_app/authors.html', context)

def books(request, id):
    context = {
        "book": Book.objects.get(id=id),
        "author": Author.objects.all(),
        "title": Book.objects.get(id=id)  
    }
    return render(request, 'books_authors_app/books.html', context)

def add_book(request):
    if request.method =="POST":
        print(request.POST)
        
    return redirect('/')

def add_author(request):
    context = {
        "author" : Author.objects.all(),
    }
    return redirect("/books/"+id, context)

def add_here(request):
    


# concatenation = adding strings to things
# "string1" + "string2"
# "string1" + str(variable)
# interpolation = inserting a variable into a string
# f"string1 {variable}"