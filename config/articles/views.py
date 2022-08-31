from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .Actions.getCategoriesAndTagsAction import getCategoriesAndTagsAction
from .forms import AddPostForm, RegisterUserForm
from .models import *


class ArticlesList(ListView):
    paginate_by = 1
    model = Article
    context_object_name = 'posts'
    cats, tags = getCategoriesAndTagsAction.execute()
    extra_context = {'cats': cats, 'tags': tags}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Article.objects.filter(is_published=True).select_related('cat')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'articles/register.html'
    success_url = reverse_lazy('login')

    cats, tags = getCategoriesAndTagsAction.execute()
    extra_context = {'cats': cats, 'tags': tags}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ArticleAdd(CreateView):
    form_class = AddPostForm
    template_name = 'articles/add.html'


class CategoryList(ListView):
    paginate_by = 3
    model = Category
    context_object_name = 'posts'
    template_name = 'articles/article_list.html'

    cats, tags = getCategoriesAndTagsAction.execute()
    extra_context = {'cats': cats, 'tags': tags}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Article.objects.filter(cat__slug=self.kwargs['slug']).select_related('cat')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'articles/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    cats, tags = getCategoriesAndTagsAction.execute()
    extra_context = {'cats': cats, 'tags': tags}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TagList(ListView):
    paginate_by = 3
    model = Tag
    context_object_name = 'posts'
    template_name = 'articles/article_list.html'

    cats, tags = getCategoriesAndTagsAction.execute()

    extra_context = {'cats': cats, 'tags': tags}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Article.objects.filter(tags__pk=self.kwargs['id']).select_related('cat')


class ArticleShow(DetailView):
    model = Article
    context_object_name = 'p'
    template_name = 'articles/show.html'

    cats, tags = getCategoriesAndTagsAction.execute()

    extra_context = {'cats': cats, 'tags': tags}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def destroy(request, id):
    record = get_object_or_404(Article, pk=id)
    record.delete()
    return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('home')
