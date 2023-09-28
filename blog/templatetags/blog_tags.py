from django import template

register = template.Library()

@register.inclusion_tag('blog/popular-post.html')
def latestpost():
    posts = posts.object.fillter(status=1).oreder_by('published_date')[:3]
    return {'posts':posts}