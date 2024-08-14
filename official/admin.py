from django.contrib import admin
from .models import Official, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Official)
class OfficialAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Comment)