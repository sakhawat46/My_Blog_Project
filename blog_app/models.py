from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=255, verbose_name='Put a Title')
    slug = models.SlugField(max_length=255, unique=True)
    blog_content = models.TextField(verbose_name='what is your mind!!')
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Image', blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date',]

    def __str__(self):
        return str(self.blog_title)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)

    def __str__(self):
        return str(self.comment)


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_liked')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_liked')

    def __str__(self):
        return str(self.user)