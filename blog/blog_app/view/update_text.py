from django.shortcuts import render, redirect, get_object_or_404
from blog_app.forms import  UpdateTextForm
from django.contrib.auth.decorators import login_required
from blog_app.models import TextModel


@login_required(login_url='/')
def update_text(request, slug):
    text = get_object_or_404(TextModel, slug= slug, author= request.user)
    form = UpdateTextForm(request.POST or None, files=request.FILES or None, instance=text)
    if form.is_valid():
        form.save()
        return redirect('detail', slug= text.slug)
    return render(request, 'pages/update_text.html', context={'form': form})
