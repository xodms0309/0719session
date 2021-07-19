from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs=Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    details=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

#new.html을 띄워주는 함수
def new(request):
    return render(request, 'new.html') 

#입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    blog=Blog() #블로그 객체 생성
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id)) #다 처리하고 이 URL로 이동하세요
    #URL은 문자열이기 때문에 형변환을 해준다!