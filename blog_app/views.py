from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.


class PostListView(ListView):
	model = Post
	template_name = 'blog_app/index.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post

def about(request):
	return render(request,'blog_app/about.html')