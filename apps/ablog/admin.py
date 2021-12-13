from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Category, Comment

# Register your models here.
#admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'img')
    search_fields = ('title', 'author', 'created_on')
    list_per_page = 25
    
    readonlyfields = ['post_image']
    
    def post_image(self,obj):
        return mark_safe(
            '<a href="{url}"> <img src="{url}" width="20%"/> </a>'.format(url=obj.img.url,)
        )
admin.site.register(Post,PostAdmin)