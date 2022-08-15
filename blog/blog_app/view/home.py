from django.shortcuts import render
from blog_app.models import TextModel
from django.core.paginator import Paginator

def home(request):
    text = TextModel.objects.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(text,2)
    
    return render (request,'pages/index.html',context={
        'texts' : paginator.get_page(page)
        })
    