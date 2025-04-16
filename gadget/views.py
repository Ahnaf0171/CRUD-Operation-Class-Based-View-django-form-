from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, UpdateView,CreateView, DeleteView
from gadget.models import Gadgets
from django.urls import reverse_lazy
from gadget.forms import GadgetsForm

# Create your views here.
class home(ListView):
    model = Gadgets
    template_name = 'home.html'
    context_object_name = 'gadgets'

class Add_gadget(CreateView):
    form_class = GadgetsForm
    template_name = 'create.html'
    success_url =reverse_lazy('home') 

class Update_view(UpdateView):
    model = Gadgets
    form_class= GadgetsForm
    template_name = 'create.html'
    success_url =reverse_lazy('home') 
    context_object_name = 'gadget'
    pk_url_kwarg = 'id'

class Delete_view(DeleteView):
    model=Gadgets
    template_name='delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    context_object_name = 'gadget'

    

    