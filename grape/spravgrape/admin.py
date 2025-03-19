from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import SortGrape, InfoGrape


# Register your models here.





class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(SortGrape, PostAdmin)
admin.site.register(InfoGrape, PostAdmin)