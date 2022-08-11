from django.contrib import admin
from blog_app.models import CategoryModel, TextModel

admin.site.register(CategoryModel)

class TextAdmin(admin.ModelAdmin):
    search_fields = ('title', 'context')
    list_display = (
        'title',
        'created_at',
        'updated_at'
    )
admin.site.register(TextModel, TextAdmin)
# Register your models here.
