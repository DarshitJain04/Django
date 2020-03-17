from django.shortcuts import render, redirect
from .models import *
from .forms import *

def Todohome(request):
	tasks=Task.objects.all()

	form = TaskForm()

	context={'tasks':tasks , 'form':form}

	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('TodoHome') 	

	return render(request,'todo/list.html',context)
