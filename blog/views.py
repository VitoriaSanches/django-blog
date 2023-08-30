from django.views.generic.detail import DetailView

from blog.models import Post

from django.shortcuts import render

from django.http import HttpResponse

from blog.models import Post


def index(request):
    return render(request, "index.html", {"titulo": "Últimos Artigos"})


def ola(request):
    # return HttpResponse('Olá Django')
    return render(request, "home.html")


def ola(request):  # Modificar
    # return HttpResponse('Olá django')
    posts = Post.objects.all()  # recupera todos os posts do banco de dados
    context = {"posts_list": posts}  # cria um dicionário com os dado
    return render(
        request, "posts.html", context
    )  # renderiza o template e passa o contexto


from django.shortcuts import render, get_object_or_404
from blog.models import Post


def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post/detail.html", {"post": post})


class PostDetailView(DetailView):
    model = Post
    template_name = "post/detail.html"
    context_object_name = "post"
