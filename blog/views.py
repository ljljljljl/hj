from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog_page(request):
    blogs=Blog.objects
    return render(request,'blog.html',{'blog':blogs})


def blog_text(request, blog_id):
    
    return render(request,'blog_text.html')
