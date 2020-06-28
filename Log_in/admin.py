from django.contrib import admin
from .models import Materials
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class MaterialsAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {"fields": ["materials_title", "materials_published"]}),
        ("Content", {"fields": ["materials_content"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget':TinyMCE()}
    }

admin.site.register(Materials,MaterialsAdmin)
