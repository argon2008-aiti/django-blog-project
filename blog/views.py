"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader, Template
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Post, Comment, Blog


def post_list(request):
    posts = Post.objects.all()
    t = loader.get_template('blog/post_list.html')
    c = Context({'posts':posts })
    return HttpResponse(t.render(c))
    
def post_detail(request, id, showComments):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=id) 
    t = loader.get_template('blog/post_detail.html')
    c = Context({'post':post, 'comments':comments})
    return HttpResponse(t.render(c))

def post_search( request, term ):
    posts = Post.objects.filter(title__contains = term)
    return render_to_response('blog/post_search.html',{'posts':posts, 'term':term})
    
def home(request):
   blog = Blog() 
   return render_to_response('blog/base.html',{'blog':blog}) 

