from django.contrib import admin
from .models import Football, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Football)
class FootballAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)


