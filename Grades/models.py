# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
PROJECT_CHOICES = (
    ('django','DJANGO'),
    ('kivy', 'KIVY'),
    ('custom', 'CUSTOM'),
)
class Student(models.Model):
    nume=models.CharField(max_length=30)
    prenume=models.CharField(max_length=30)
    #poza=models.ImageField(upload_to='poze/', default='avatar.png', null=True, blank=True)
    # proiect=models.FileField(upload_to='proiecte/',null=True, blank=True)
    # tip_proiect = models.CharField(max_length=6, choices=PROJECT_CHOICES, default='django')
    an=models.IntegerField(default=1)
    materie1 = models.CharField(max_length=40, default='Geometrie computationala')
    nota1 = models.IntegerField(default=0)
    materie2 = models.CharField(max_length=40, default='Calculabilitate si complexitate')
    nota2 = models.IntegerField(default=0)
    materie3 = models.CharField(max_length=40, default='Tehnici web')
    nota3 = models.IntegerField(default=0)
    materie4 = models.CharField(max_length=40, default='Tehnici avansate de programare')
    nota4 = models.IntegerField(default=0)
    materie5 = models.CharField(max_length=40, default='Probabilitate si statistica')
    nota5 = models.IntegerField(default=0)
    materie6 = models.CharField(max_length=40, default='Sisteme de operare')
    nota6 = models.IntegerField(default=0)
    email=models.EmailField(unique=True)
    medie=models.IntegerField(default=0)

class Professor(models.Model):
    nume=models.CharField(max_length=30)
    prenume=models.CharField(max_length=30)
   # poza=models.ImageField(upload_to='poze/', default='avatar.png', null=True, blank=True)
    materie = models.CharField(max_length=40, default=' ')
    credite=models.IntegerField(default=0)
    email=models.EmailField(unique=True)

# class zzz(models.Model):
#
#     sursa = ManyToManyField()
#     # nume=models.AutoField(primary_key=True)
#     # materie= models.ForeignKey("materie",  db_column="materie1")
#     # nota=models.ForeignKey(default=0)

# class A(models.Model):
#     titlu = models.CharField(max_length=30)


# class B:
#     headline = models.CharField(max_length=30)
#     publicatii = models.ManyToManyField(A)
#
#     class Meta:
#         ordering = ['headline']

# class Publication(models.Model):
#     title = models.CharField(max_length=30)
#
#     class Meta:
#         ordering = ['title']
#
#     def __str__(self):
#         return self.title

# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     publications = models.ManyToManyField(Publication)
#
#     class Meta:
#         ordering = ['headline']
#
#     def __str__(self):
#         return self.headline

# p1 = Publication(title='The Python Journal')
# p1.save()
# p2 = Publication(title='Science News')
# p2.save()
# p3 = Publication(title='Science Weekly')
# p3.save()
# a1 = Article(headline='Django lets you build Web apps easily')
# a1.save()
# a1.publications.add(p1)
# a2 = Article(headline='NASA uses Python')
# a2.save()
# a2.publications.add(p1, p2)
# a2.publications.add(p3)
# a2.publications.add(p3)