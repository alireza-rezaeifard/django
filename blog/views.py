from django.shortcuts import get_object_or_404, render
from blog.models import post

# Create your views here.
def blog_view(request) :
    posts = post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request, pid):
    posts = get_object_or_404(post, pk=pid)
    context = {'posts': posts}
    return render(request, 'blog/blog-single.html', context)