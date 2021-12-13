from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.safestring import mark_safe

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    img= models.ImageField(null=True, blank=True, upload_to='img/portfolio', help_text="Seleccione una imagen para mostrar")
    created_on = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        #return reverse('apps.blog:blog_detail', args=(str(self.id)))
        return reverse("apps.ablog:blog_detail",kwargs={'id':self.pk})


    def __str__(self):
        return self.title
    
    def image_display(self):
        return mark_safe(
            '<a href="{url}"> <img src="{url}" width="20%"/> </a>'.format(url=obj.img.url,)
        )
    image_display.allow_tags = True
    image_display.short_description= u'IMAGE'


class Comment(models.Model):
    post = models.ForeignKey('ablog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    #def __str__(self):
        #return self.text
    