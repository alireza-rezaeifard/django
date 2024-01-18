from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import post


class LatestEntriesFeed(Feed):
    title = "Blog newest posts"
    link = "/rss/feed"
    description = "Best blog ever."

    def items(self):
        return post.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]

    # # item_link is only needed if NewsItem has no get_absolute_url method.
    # def item_link(self, item):
    #     return reverse("news-item", args=[item.pk])
