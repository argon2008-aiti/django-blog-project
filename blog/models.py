from django.db import models
from django.contrib import admin

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    updated = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)
     
    def get_absolute_url(self):
        return "/blog/posts/%i/true" % self.id


    def __unicode__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    author = models.CharField(max_length=60)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post)

    def get_absolute_url(self):
        return "/blog/posts/%i/true" %self.post.id
        
    def __unicode__(self):
        return self.body

class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created','updated',)
    search_fields = ('title','body',)
    list_filter = ('created',)
    inlines = [ CommentInline, ]
                
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','author','body'[:60],'created','updated',)
    list_filter = ('created','author',)
    
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)

