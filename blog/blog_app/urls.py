import imp
from unicodedata import name
from django.urls import path
from blog_app.view import contact
from blog_app.view import home, CategoryListView, my_text, DetailView,add_text,update_text,delete_text
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
    path('contact/', contact, name='contact'),
    # ==================================================

    path('category/<slug:categorySlug>', CategoryListView.as_view(), name='category'),
    # ==================================================
 
    path('mytext/', my_text, name='mytext'),
    # ====================class view larda as_view() sakın ınutma==============================

    path('detail/<slug:slug>', DetailView.as_view(), name='detail'),
    # ==================================================

    path('add-text/', add_text, name='add_text'),
    # ==================================================

    path('update-text/<slug:slug>', update_text ,name='update_text'),
    # ==================================================

    path('delete-text/<slug:slug>', delete_text ,name='delete_text'),
    # ==================================================

    path('delete-comment/<int:id>', delete_comment ,name='delete_comment'),
]
