import imp
from unicodedata import name
from django.urls import path
from blog_app.view import ContactFormView
from blog_app.view import home, CategoryListView, my_text, DetailView,AddTextCreateView,UpdateTextUpdateView,DeleteTextDeleteView
from .view.delete_comment import delete_comment
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', home, name='home'),
    # Template view kullanımı============================

    path('about/', TemplateView.as_view(
        template_name= 'pages/about.html'
        ), name='about'),
    # Redirect view kullanımı============================
    path('redirect/', RedirectView.as_view(
        url='http://www.google.com'
        ), name='redirect'),
    # ==================================================
    path('contact/', ContactFormView.as_view(), name='contact'),
    # ==================================================

    path('category/<slug:categorySlug>', CategoryListView.as_view(), name='category'),
    # ==================================================
 
    path('mytext/', my_text, name='mytext'),
    # ====================class view larda as_view() sakın ınutma==============================

    path('detail/<slug:slug>', DetailView.as_view(), name='detail'),
    # ==================================================

    path('add-text/', AddTextCreateView.as_view(), name='add_text'),
    # ==================================================

    path('update-text/<slug:slug>', UpdateTextUpdateView.as_view() ,name='update_text'),
    # ==================================================

    path('delete-text/<slug:slug>', DeleteTextDeleteView.as_view() ,name='delete_text'),
    # ==================================================

    path('delete-comment/<int:id>', delete_comment ,name='delete_comment'),
    
    path('email-submited', TemplateView.as_view(
        template_name= 'pages/email-submited.html'
        ), name='email-submited')
]
