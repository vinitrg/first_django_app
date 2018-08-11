from django.urls import path
from . import views

urlpatterns = [
	path('',views.publish_list, name='publish_list')
	#path('',views.post_list, name='post_list')
]