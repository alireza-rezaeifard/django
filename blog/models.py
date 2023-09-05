from django.db import models

# Create your models here.

class post(models.Model) :
    #image
    #author = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tag
    #categori
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta :
        ordering = ['created_date']
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
    
    def __str__(self):
        return self.title