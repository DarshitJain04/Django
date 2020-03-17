from django.urls import path
from . import views

urlpatterns=[
	path('',views.Todohome,name='TodoHome'),
]