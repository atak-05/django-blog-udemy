from atexit import register
from django import template
from blog_app.models import CategoryModel

#Kendi taglarimizi bu şekilde oluşturabiliyoruz!
register = template.Library()

@register.simple_tag
def category_list():
    categories = CategoryModel.objects.all()
    return categories