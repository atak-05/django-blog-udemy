from django.shortcuts import render, get_object_or_404
from blog_app.models import TextModel, CommentModel

def detail(request,slug):
    text =get_object_or_404(TextModel, slug=slug)
    comments = text.comments.all()
    return render(request, 'pages/detail.html', context = {
        'text' : text,
        'comments' : comments})
    
   