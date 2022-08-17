from django.shortcuts import render, get_object_or_404
from blog_app.models import TextModel, CommentModel
from blog_app.forms import AddCommentForm
def detail(request,slug):
    text =get_object_or_404(TextModel, slug=slug)
    comments = text.comments.all()
    if request.method=='POST':
        add_comment_form = AddCommentForm(data=request.POST)
        if add_comment_form.is_valid():
            comment= add_comment_form.save(commit=False)
            comment.writer= request.user
            comment.text= text
            comment.save()

    add_comment_form= AddCommentForm
    
   
    return render(request, 'pages/detail.html', context = {
        'text' : text,
        'comments' : comments,
        'add_comment_form': add_comment_form})
    
   