from django.contrib.auth.decorators import login_required
from blog_app.models import CommentModel
from django.shortcuts import get_object_or_404,redirect
# Message Framework in Django
from django.contrib import messages



@login_required(login_url='/')
def delete_comment (request, id):
    comment = get_object_or_404(CommentModel, id=id)
    if comment.writer == request.user or comment.text.author == request.user:
        comment.delete()
        # Message Framework in Django
        messages.success(request, 'Your comment has been successfully deleted')
        return redirect('detail', slug=comment.text.slug)
    
    return redirect('home')