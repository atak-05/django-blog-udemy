from django.shortcuts import render, get_object_or_404
from blog_app.models import TextModel, CategoryModel
from django.core.paginator import Paginator
from django.views.generic import ListView

# Bu kısım  da djangonun LİSTVİEW özelliğinden yararlanılmıştır
class CategoryListView(ListView):
    template_name = 'pages/category.html'
    context_object_name = 'texts'
    
    def get_queryset(self) :
        category = get_object_or_404(CategoryModel, slug = self.kwargs['categorySlug'])   
        return category.texts.all()
# Bu kısım  klasik yöntemdir.

# def category(request, categorySlug):
#     category= get_object_or_404(CategoryModel, slug= categorySlug)
#     text = category.text.order_by("-id")
#     page = request.GET.get('page')
#     paginator = Paginator(text,2)
    
#     return render (request,'pages/category.html',context={
#         'texts' : paginator.get_page(page),
#         'category_title' :category.title
#         })
    