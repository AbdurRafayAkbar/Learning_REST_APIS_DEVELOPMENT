from django.db import models

class Blogs(models.Model):
    blog_title=models.CharField(max_length=50)
    blog_description=models.TextField()

    def __str__(self):
        return self.blog_title
    
