from django.shortcuts import get_object_or_404, render
from blog.models import post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.



def blog_view(request, **kwargs):
    posts = post.objects.filter(status=1)
    print(kwargs)
    if kwargs.get("cat_name") != None:
        posts = posts.filter(category__name=kwargs["cat_name"])
    if kwargs.get("author_username") != None:
        posts = posts.filter(author__username=kwargs["author_username"])
    if kwargs.get("tag_name") != None:
        posts = posts.filter(tags__name__in=[kwargs["tag_name"]])

    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {
        "posts": posts,
    }
    return render(request, "blog/blog-home.html", context)

    
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

def blog_search(request):
    posts = post.objects.filter(status=1) 
    if request.method == "GET":
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
        
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)