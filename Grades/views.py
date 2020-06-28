# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


#
# def index(request):
#     return HttpResponse('<p>Index view</p>')
#
#
# def entry_detail(request, *id_ul):
#     return HttpResponse('<p>entry_detail cu nume ' + str(id_ul) + ' </p>')
#
#
# def contact(request):
#     return_string = '''<h3>Contact</h3>
# <p>Contact: Numele Tau</p>
# <p>Email:office@site.com</p>
# <p>Tel:070.111.111</p>'''
#     return HttpResponse(return_string)


from django.http import Http404
from Grades.models import Student


def index(request):
    intrari = Student.objects.all()
    return render(request, 'base.html', {'entryS': intrari})


# def contact(request):
#     return render(request, 'contact.html', {})
#
#
# # from main.Forms import ContactForm
# from django.conf import settings
# from django.core.mail import send_mail
#
#
# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             mesaj = "Mesaj de la:" + form.cleaned_data['contact_name'] + ",email:" + \
#                     form.cleaned_data['contact_email'] + "\n\n" + \
#                     form.cleaned_data['content']
#             send_mail('Contact prin django', mesaj, settings.EMAIL_HOST_USER, ['mail.through.python@gmail.com'],
#                       fail_silently=False)
#         return render(request, 'contact_send.html', {})
#     else:
#         return render(request, 'contact.html', {'form': ContactForm})
