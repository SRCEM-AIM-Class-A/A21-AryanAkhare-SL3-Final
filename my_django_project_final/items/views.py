from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def homepage(request):
    items = Item.objects.all()
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    return render(request, 'items/homepage.html', {'items': items, 'form': form})
