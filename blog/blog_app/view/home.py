from turtle import title
from django.shortcuts import render
from blog_app.models import TextModel
from django.core.paginator import Paginator
from django.db.models import Q

def home(request):
    search = request.GET.get('search')
    text = TextModel.objects.order_by('-id')
    if search:     
        text = text.filter(
            Q(title__icontains = search) |
            Q(context__icontains = search)
        ).distinct()  

    page = request.GET.get('page')
    paginator = Paginator(text,2)
        
    return render (request,'pages/index.html',context={
        'texts' : paginator.get_page(page)
        })
    