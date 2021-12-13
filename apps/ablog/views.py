from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import( TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)

# Create your views here.
def index(request):
    html = '<html><body><p>Hola mundo!!!!</p></body></html>'
    return HttpResponse(html)

def blog_index(request):
    post_list = Post.objects.all().order_by('-created_on')
    context = {
        "posts": post_list,
    }
    return render(request, "blog_index.html", context)

def blog_detail(request, id):
    post = Post.objects.get(id=id)

    form=CommentForm()
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.isvalid():
            print("Validacion exitosa!")
            print("Autor:" + form.cleaned_data["author"])
            print("Comentario:" + form.cleaned_data["comment_body"])
            comment = Comment(
                author=form.cleaned_data["author"],
                comment_body=form.cleaned_data["comment_body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, 'blog_detail.html', context)