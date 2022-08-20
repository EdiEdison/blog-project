from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView


# this function-based view
# def home(request):
# context = {
# 'posts': Post.objects.all()
# }
# return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['posts'] = context['posts'].filter(title__icontains=search_input)
            context['search_input'] = search_input
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'posts'
