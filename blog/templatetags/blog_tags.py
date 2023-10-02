from django import template
from blog.models import post,category
register = template.Library()

@register.inclusion_tag('blog/popular-post.html')
def latestpost():
    global posts
    posts = post.objects.filter(status=1).order_by('published_date')[:4]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-category.html')
def postcat():
    posts = post.objects.filter(status=1)
    categories = category.objects.all()
    cat_dict = {}
    
    for name in categories :
        cat_dict[name] = posts.filter(category=name).count()
    
    return {'categories':cat_dict}
    
