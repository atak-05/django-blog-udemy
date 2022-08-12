from django.contrib import admin
from blog_app.models import CategoryModel, TextModel, CommentModel, ContactModel

admin.site.register(CategoryModel)

#=========================Text-Admin==============================#
@admin.register(TextModel)
class TextAdmin(admin.ModelAdmin):
    search_fields = ('title', 'context')
    list_display = (
        'title',
        'created_at',
        'updated_at'
    )
# Register your models here.

#=========================Comment-Admin==============================#

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('writer',
                    'created_at',
                    'updated_at'
                    )
    search_fields = ('writer__username',)
    
#=========================Contact-Admin==============================#
@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email',
                    'created_at'
                    )
    search_fields = ('email',)
