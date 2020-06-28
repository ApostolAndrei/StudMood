from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Grades.models import *

class studentAdmin(admin.ModelAdmin):
    list_display=["nume","email","an",
                  "materie1","nota1",
                  "materie2","nota2",
                  "materie3","nota3",
                  "materie4","nota4",
                  "materie5","nota5",
                  "materie6","nota6",
                  "medie"]

class professorAdmin(admin.ModelAdmin):
    list_display=["nume","materie","credite","email"]

# class zzzAdmin(admin.ModelAdmin):
#     list_display=["nume","materie","nota"]

# admin.site.register(zzz,zzzAdmin)
#
# class aAdmin(admin.ModelAdmin):
#     list_display=["titlu"]
#
# admin.site.register(A,aAdmin)

# class bAdmin():
#     list_display=["headline"]
#
# admin.site.register(B,bAdmin)

admin.site.register(Student,studentAdmin)
admin.site.register(Professor,professorAdmin)

# class publicationAdmin(admin.ModelAdmin):
#     list_display=["title"]

# admin.site.register(Publication,publicationAdmin)

# class articleAdmin(admin.ModelAdmin):
#     list_display=["headline"]
#
# admin.site.register(Article,articleAdmin)