from django.shortcuts import render
from .models import Item
from django.views.generic import ListView,CreateView,DeleteView,DetailView





class Home(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'main.html'


class New(CreateView):
    model = Item
    fields = ['name','description','timelimit']
    template_name = 'newlist.html'


class Delete(DeleteView):
    model = Item
    context_object_name = 'item'
    template_name = 'delete.html'
    success_url = '/'


class Detail(DetailView):
    model = Item
    template_name = 'detail.html'
    context_object_name = 'items'


