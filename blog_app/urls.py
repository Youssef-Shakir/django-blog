from django.urls import path
from blog_app import views
from .views import PostListView,PostDetailView
app_name = 'blog_app'

urlpatterns = [
	path('',PostListView.as_view(),name='home'),
	path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),	
	path('about/',views.about,name='about'),
]