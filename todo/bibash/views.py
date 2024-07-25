from django.shortcuts import render
from django.shortcuts import redirect
# from django.http import HttpResponse
from .models import Todo

# Create your views here.
def home(request):
    # return HttpResponse('This is my homepage')
    # return render(request, 'index.html')
    todo_objects = Todo.objects.all()
    data = {'todo':todo_objects}
    return render(request, 'index.html', context=data)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')

        Todo.objects.create(name=name, description=description, status=status)
        
        return redirect('home')

    return render(request, 'create.html')

def edit(request):
    return render(request, 'edit.html')