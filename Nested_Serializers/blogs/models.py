from django.db import models

class Blogs(models.Model):
    blog_title=models.CharField(max_length=100)
    blog_text=models.TextField()

    def __str__(self):
        return self.blog_title

class Comments(models.Model):
    blogs = models.ForeignKey(Blogs,on_delete=models.CASCADE,related_name="comments")
    comments=models.TextField()

    def __str__(self):
        return self.comments
