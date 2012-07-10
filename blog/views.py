"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader, Template
from django.http import HttpResponse

from models import Post, Comment


def post_list(request):
    post_list = Post.objects.all()
    print type(post_list)
    print post_list
    response = HttpResponse()
    response.write('<h2>POSTS</h2>')
    for post in post_list:
        response.write(post)
        response.write('</p>')
    return response

def post_detail(request, id, showComments):
    post_matched = Post.objects.get(id=id)
    post_details = post_matched.body
    post_comment = Comment.objects.get(post=id)
    response = HttpResponse() 
    post_html = Template('<h2>{{post_matched}}</h2>')
    c_1 = Context({'post_matched':post_matched})
    response.write(post_html.render(c_1))    
    response.write(post_details)

    if showComments=='true':    
        response.write('<h3>Comments</h3>')
        response.write(post_comment)
        return response
    return response

def post_search(request, anything):
    search_result = Post.objects.filter(body__contains=anything)
    t = Template('<h3>All posts containing "{{anything}}"</h3>')
    c = Context({'anything':anything})
    response = HttpResponse()
    response.write(t.render(c))
    for post in search_result:
        response.write(post.body)
        response.write('</p>')
    return response

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
