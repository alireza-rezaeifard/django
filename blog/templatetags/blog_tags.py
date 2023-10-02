from django import template
from blog.models import post
register = template.Library()

@register.inclusion_tag('blog/popular-post.html')
def latestpost():
    global posts
    posts = post.objects.filter(status=1).order_by('published_date')[:4]
    return {'posts':posts}