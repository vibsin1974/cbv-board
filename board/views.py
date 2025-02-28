from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import Board

# class Create(CreateView):
#     model = Board
#     fields =["title","writer","content","file"]
#     success_url = reverse("")

class List(ListView):
    model = Board

class Detail(DetailView):
    model = Board
    
class Create(CreateView):
    model = Board
    fields = ["title","writer","content","file"]
    success_url = "/board/"
    
    def get_form(self):
        form = super().get_form()
        form.fields["title"].label = "제목"
        form.fields["writer"].label = "작성자"
        form.fields["content"].label = "내용"
        form.fields["file"].label = "파일"
        return form