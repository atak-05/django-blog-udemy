from django.shortcuts import render, get_object_or_404, redirect
from blog_app.models import TextModel, CommentModel, comment
from blog_app.forms import AddCommentForm
from django.views import View
from django.contrib import messages

class DetailView(View):
    http_method_names = ['get', 'post']
    def get (self, request, slug):
        text =get_object_or_404(TextModel, slug=slug)
        add_comment_form = AddCommentForm
        comments = text.comments.all()
        return render(request,'pages/detail.html', context={
            'text' : text,
            'comments' : comments,
            'add_comment_form': add_comment_form() 
        })
    def post (self,request,slug):
        text =get_object_or_404(TextModel, slug=slug)
        add_comment_form = AddCommentForm(data=request.POST)
        if add_comment_form.is_valid():
            comment = add_comment_form.save(commit=False)
            comment.writer = request.user
            comment.text = text
            comment.save()
            messages.success(request, 'Your comment has been successfully added.')
        return redirect ('detail', slug= slug)
            








   