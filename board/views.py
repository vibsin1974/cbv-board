from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import Board

# class Create(CreateView):
#     model = Board
#     fields =["title","writer","content","file"]
#     success_url = reverse("")

class List(ListView):
    model = Board
        