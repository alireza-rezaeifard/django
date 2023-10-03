from django.shortcuts import get_object_or_404, render
from blog.models import post

# Create your views here.
def blog_view(request, cat_name=None, author_username=None) :
    posts = post.objects.filter(status=1)    
    if cat_name :
        posts = posts.filter(category__name=cat_name)
    if author_username :
        posts = posts.filter(author__username=author_username)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request, pid):
    post_s = post.objects.filter(status=1)
    posts = get_object_or_404(post_s, pk=pid)
    context = {'posts': posts}
    return render(request, 'blog/blog-single.html', context)

def blog_cat(request, cat_name):
    posts = post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)