from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
import pdb

# Create your views here.


def post_detail(request, post_id):
    post = _getPost(post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_new(request):
    if request.method == "POST":
        form = _createForm(request, None)
        _savePost(request, form)
        return redirect('blog.views.post_detail', post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, post_id):
    if not request.user.is_authenticated():
        return redirect('blog.views.post_detail', post_id=post_id)
    post = _getPost(post_id)
    if request.method == "POST":
        form = _createForm(request, post)
        _savePost(request, form)
        return redirect('blog.views.post_detail', post_id=post.pk)
    else :
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def _getPost(post_id):
    return get_object_or_404(Post, pk=post_id)

def _createForm(request, post):
    if not post == None:
        return PostForm(request.POST, instance=post)
    else:
        return PostForm(request.POST)

def _savePost(request, form):
    if not form == None and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        if request.POST.get('published_date', 'off') == 'on':
            post.publish()
        else:
            post.unpublish()
