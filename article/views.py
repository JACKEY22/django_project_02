

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from article.decorators import article_ownership_required
from article.forms import ArticleCreateForm
from article.models import Article

permission = [login_required, article_ownership_required]

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'article/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article:detail', kwargs={'pk':self.object.pk})

class ArticleListView(ListView):
    model = Article
    template_name = 'article/list.html'
    context_object_name = 'article_list'
    paginate_by = 50

    def get_queryset(self):
        return Article.objects.all()

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'target_article'

@method_decorator(permission, 'get')
@method_decorator(permission, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'article/create.html'
    context_object_name = 'target_article'

    def get_success_url(self):
        return reverse('article:detail', kwargs={'pk':self.object.pk})

@method_decorator(permission, 'get')
@method_decorator(permission, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article/delete.html'
    context_object_name = 'target_article'
    success_url = reverse_lazy('account:detail')

    def get_success_url(self):
        return reverse('account:detail', kwargs={'pk':self.object.writer.pk})


