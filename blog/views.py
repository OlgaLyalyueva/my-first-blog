from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect



# Create your views here.

def main(request):
    return render(request, 'blog/main.html')

def breakdance(request):
    return render(request, 'blog/breakdance.html')

def contemporary(request):
    return render(request, 'blog/contemporary.html')

def hiphop(request):
    return render(request, 'blog/hiphop.html')

def aerial_silks(request):
    return render(request, 'blog/aerial_silks.html')

def detskaya_horeografiya(request):
    return render(request, 'blog/detskaya_horeografiya.html')

def modern(request):
    return render(request, 'blog/modern.html')

def jazzfunk(request):
    return render(request, 'blog/jazzfunk.html')

def latina(request):
    return render(request, 'blog/latina.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
