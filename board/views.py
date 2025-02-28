from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import Board
from django.urls import reverse, reverse_lazy

# class Create(CreateView):
#     model = Board
#     fields =["title","writer","content","file"]
#     success_url = reverse("")

class List(ListView):
    model = Board

class Detail(DetailView):
    model = Board
    
    def get_object(self):
        object = super().get_object()
        object.add_count()
        return object
    
    
class Create(CreateView):
    model = Board
    fields = ["title","writer","content","file"]
    success_url = reverse_lazy("board:list")
    
    def get_form(self):
        form = super().get_form()
        form.fields["title"].label = "제목"
        form.fields["writer"].label = "작성자"
        form.fields["content"].label = "내용"
        form.fields["file"].label = "파일"
        return form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["button_lbl"] ="쓰기"
        return context
    
    
    
class Edit(UpdateView):
    model = Board
    fields = ["title","writer","content","file"]
    success_url = reverse_lazy("board:list")
    
    def get_form(self):
        form = super().get_form()
        form.fields["title"].label = "제목"
        form.fields["writer"].label = "작성자"
        form.fields["writer"].disabled = True
        form.fields["content"].label = "내용"
        form.fields["file"].label = "파일"
        return form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["button_lbl"] ="수정"
        return context
    
class Delete(DeleteView):
    model = Board
    success_url = reverse_lazy("board:list")
    