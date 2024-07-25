from django.shortcuts import render, redirect

from .forms import BookForm
from .models import Book

def index(request):
    books = Book.objects.all()

    return render(request, 'book/index.html', {
        'books':books
    })

def detail(request, pk):
    book = Book.objects.get(pk=pk)

    return render(request, 'book/detail.html', {
        'book': book
    })



def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('book:index')
    else:
        form = BookForm()
    

    return render(request, 'book/add.html', {
        'form': form
    })