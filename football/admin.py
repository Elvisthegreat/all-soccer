from django.contrib import admin
from .models import Football
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Football)
class FootballAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

