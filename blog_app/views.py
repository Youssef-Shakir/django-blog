from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.


class PostListView(ListView):
	model = Post
	template_name = 'blog_app/index.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post

class PostDeleteView(DeleteView):
	model = Post
	success_url = '/'

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields = ['title','content']

	def test_func(self):
		post = self.get_object()
		if post.author == self.request.user:
			return True
		return False
	

def about(request):
	return render(request,'blog_app/about.html')