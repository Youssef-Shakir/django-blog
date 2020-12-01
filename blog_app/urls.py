from django.urls import path
from blog_app import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
app_name = 'blog_app'

urlpatterns = [
	path('',PostListView.as_view(),name='home'),
	path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),	
	path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),	
	path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
	path('post/new/',PostCreateView.as_view(),name='post-create'),	
	path('about/',views.about,name='about'),
]