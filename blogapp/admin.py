from django.contrib import admin
from blogapp.models import *

# Register your models here.
class blogpostAdmin(admin.ModelAdmin):
    list_display = 'title','category','content'

admin.site.register(Blogpost,blogpostAdmin)