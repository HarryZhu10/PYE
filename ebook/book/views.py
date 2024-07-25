from django.shortcuts import render, redirect

from .forms import BookForm


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