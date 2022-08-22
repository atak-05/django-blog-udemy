from django.shortcuts import render, redirect, get_object_or_404
from blog_app.forms import  UpdateTextForm
from django.contrib.auth.decorators import login_required
from blog_app.models import TextModel
from django.views.generic import UpdateView
from django.urls import reverse

class UpdateTextUpdateView(UpdateView):
    template_name = 'pages/update_text.html'
    fields = ('title' , 'image' , 'context', 'categories')
    def get_object(self):
        text = get_object_or_404(
            TextModel,
            slug = self.kwargs.get('slug'),
            author = self.request.user
        )
        return text
    def get_success_url(self):
        return reverse('detail' , kwargs={
            'slug' : self.get_object().slug
        })


@login_required(login_url='/')
def update_text(request, slug):
    text = get_object_or_404(TextModel, slug= slug, author= request.user)
    form = UpdateTextForm(request.POST or None, files=request.FILES or None, instance=text)
    if form.is_valid():
        form.save()
        return redirect('detail', slug= text.slug)
    return render(request, 'pages/update_text.html', context={'form': form})
