from django.shortcuts import render, redirect
from blog_app.forms import AddTextForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def add_text(request):
    form = AddTextForm(request.POST or None, files = request.FILES or None)
    if form.is_valid():
        text=form.save(commit=False)
        text.author = request.user
        text.save()
        form.save_m2m()
        return redirect('detail', slug=text.slug)
    return render(request, 'pages/add_text.html', context={'form': form})
