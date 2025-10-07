from django.shortcuts import render
from django.views.generic import ListView
from .models import Task
from django.shortcuts import redirect

class TaskListView(ListView):
    model = Task
    template_name = 'list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        task_id = request.POST.get('id')

        if action == 'add':
            title = request.POST.get('title', '').strip()
            if title:
                Task.objects.create(title=title)

        elif action == 'toggle' and task_id:
            try:
                t = Task.objects.get(pk=task_id)
                t.completed = not t.completed
                t.save()
            except Task.DoesNotExist:
                pass

        elif action == 'edit' and task_id:
            try:
                new_title = request.POST.get('new_title', '').strip()
                if new_title:
                    t = Task.objects.get(pk=task_id)
                    t.title = new_title
                    t.save()
            except Task.DoesNotExist:
                pass

        elif action == 'delete' and task_id:
            Task.objects.filter(pk=task_id).delete()

        return redirect('task-list')