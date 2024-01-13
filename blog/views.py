from django.shortcuts import get_object_or_404, render
from blog.models import post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.



def blog_view(request, cat_name=None, author_username=None) :
    posts = post.objects.filter(status=1)   
    #for category fillter 
    if cat_name :
        posts = posts.filter(category__name=cat_name)
    #for username author
    if author_username :
        posts = posts.filter(author__username=author_username)
        
    # for the pagination of the blog pages   
    paginator = Paginator(posts, 4)
    
    try:
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(1)        
    # end of pagination
    
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

def blog_search(request):
    posts = post.objects.filter(status=1) 
    if request.method == "GET":
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
        
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)