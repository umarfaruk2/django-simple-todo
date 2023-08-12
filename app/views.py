from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import TaskModelForm
from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import TaskModel

# Create your views here.
class AddTaskView(CreateView):
    model = TaskModel 
    form_class = TaskModelForm
    template_name = 'add_task.html'
    success_url = reverse_lazy('show_task') 

def show_task(request):
    task_data = TaskModel.objects.filter(is_complete=False)

    return render(request, 'show_task.html', {'data': task_data})

class UpdateTaskView(UpdateView):
    model = TaskModel
    form_class = TaskModelForm
    template_name = 'add_task.html'
    success_url = reverse_lazy('show_task')

class DeleteTaskView(DeleteView):
    model = TaskModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('show_task')

class CompleteTaskView(ListView):
    model = TaskModel
    template_name = 'complete_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'data': TaskModel.objects.filter(is_complete=True)}
        return context

def is_complete_task(request, id):
    task_data = TaskModel.objects.get(pk = id)
    task_data.is_complete = True 
    task_data.save()
    return redirect('complete_task') 