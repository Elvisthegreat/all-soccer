from django.contrib import admin
from .models import Official, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Official)
class OfficialAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Comment)