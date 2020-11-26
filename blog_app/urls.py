from django.urls import path
from blog_app import views
app_name = 'blog_app'

urlpatterns = [
	path('',views.index,name='home'),
	path('about/',views.about,name='about'),
]