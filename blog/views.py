"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader, Template
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Post, Comment
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
import datetime

def post_list(request):
    posts = Post.objects.all()
    t = loader.get_template('blog/post_list.html')
    c = Context({'posts':posts })
    return HttpResponse(t.render(c))

class CommentForm(forms.ModelForm):
    body = forms.CharField(label='comment',widget=forms.Textarea(attrs={'rows': 5,'style':'width:75%','text':'type comment here'}))
    class Meta:
        model = Comment
        fields = ('body',)
        
                    
        
        
@csrf_exempt    
def post_detail(request, id ):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        comment = Comment(post=post, author=request.user.username)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect( request.path )
    else:
        form = CommentForm()
    comments = Comment.objects.filter(post=id) 
    t = loader.get_template('blog/post_detail.html')
    c = Context({'post':post, 'comments':comments, 'form':form, 'user':request.user})
    return HttpResponse(t.render(c))

def post_search( request, term ):
    posts = Post.objects.filter(title__contains = term)
    return render_to_response('blog/post_search.html',{'posts':posts, 'term':term})
    
def home(request): 
   return render_to_response('blog/base.html',{}) 

@csrf_exempt
def edit_comment( request,id ):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST': 
        form = CommentForm(request.POST, instance = comment )
        if form.is_valid():
            now  = datetime.datetime.now()
            comment.updated = now.date()
            
            form.save()
        return HttpResponseRedirect( comment.get_absolute_url() )
    else:
        form = CommentForm( instance = comment )
    return render_to_response('blog/edit_comment.html', {'comment':comment,'form':form } )

