from django.urls import path
from .import views


app_name = 'main'

urlpatterns = [
	path('',views.index, name='homePage' ),
	path('contact/',views.contact, name='contactPage' ),
	path('blog/',views.blog, name='blogPage' ),
	path('blog/<str:post_slug>',views.blog_detail, name='blogDetailPage' ),

	path('search_results/', views.search, name='search'),
]

