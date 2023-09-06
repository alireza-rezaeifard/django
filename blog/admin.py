from django.contrib import admin
from blog.models import post, category

# Register your models here.
class postAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["title","author", "counted_views", "status", "published_date", "created_date", "updated_date"]
    list_filter = ('status',"author")
    ordering = ["created_date"]
    search_fields = ["title"]

    
admin.site.register(category)
admin.site.register(post,postAdmin)