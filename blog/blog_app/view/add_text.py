from urllib import request
from django.shortcuts import render, redirect
from blog_app.forms import AddTextForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from blog_app.models import TextModel
from django.urls import reverse

class AddTextCreateView(CreateView):
    template_name = 'pages/add_text.html'
    model = TextModel
    fields = ('title' , 'image' , 'context', 'categories')
    
    def get_success_url(self):
        return reverse('detail', kwargs= {
            'slug' : self.object.slug
        })
    
    def form_valid(self, form):
        text=form.save(commit=False)
        text.author = self.request.user
        text.save()
        form.save_m2m()
        return super().form_valid(form)




# @login_required(login_url='/')
# def add_text(request):
#     form = AddTextForm(request.POST or None, files = request.FILES or None)
#     if form.is_valid():
#         text=form.save(commit=False)
#         text.author = request.user
#         text.save()
#         form.save_m2m()
#         return redirect('detail', slug=text.slug)
#     return render(request, 'pages/add_text.html', context={'form': form})
