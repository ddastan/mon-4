from django.db import models

# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category', null=True, blank=True)
    tag = models.ManyToManyField('Tag', related_name='tags', blank=True)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comment', null=True)

    def __str__(self):
        return self.text