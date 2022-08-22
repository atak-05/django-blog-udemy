from re import template
from urllib import request
from django.contrib.auth.decorators import login_required
from blog_app.models import TextModel
from django.shortcuts import redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class DeleteTextDeleteView(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'pages/delete_text_confirm.html'
    success_url= reverse_lazy('mytext')
    def get_queryset(self):
        text = TextModel.objects.filter(slug=self.kwargs['slug'], author=self.request.user)
        return text  



