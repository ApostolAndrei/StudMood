from django.shortcuts import redirect,render
from django.views import generic
from .models import Post


def PostList(request):
    queryset = Post.objects.order_by("-created_on")
    context = {"post_list" : queryset}
    return render(request , "news.html" , context)


def baseView(request):
    return render(request,'base.html')



# Create your views here.
