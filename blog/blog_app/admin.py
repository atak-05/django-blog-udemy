from django.contrib import admin
from blog_app.models import CategoryModel, TextModel, CommentModel

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


class CommentAdmin(admin.ModelAdmin):
    list_display = ('writer', 
                    'created_at',
                    'updated_at'
                    )
    search_fields = ('writer__username',)


admin.site.register(CommentModel, CommentAdmin)
