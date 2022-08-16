from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog_app.models import TextModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def my_text(request):
    text = request.user.text_author.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(text, 2)

    return render(request, 'pages/my_text.html', context={
        'texts': paginator.get_page(page),
    })
