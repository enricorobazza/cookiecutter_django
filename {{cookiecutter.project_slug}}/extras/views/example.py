from django.shortcuts import redirect
from django.http import JsonResponse

from extras.models import Task
from extras.forms import CategoryForm, TaskForm
from extras.components.base import BaseView

class CategoryView():
    def add_ajax(request):
        if(request.method == 'POST'):
            form = CategoryForm(request.POST)

            if form.is_valid():
                category = form.save()
                return JsonResponse({"success": True, "content": {"id": category.pk, "text": category.name}}, safe=False)
            else:
                return JsonResponse({"success": False, "errors": form.errors}, safe=False)

class TaskView(BaseView):
    template_path="extras/views"
    table_fields=['title', 'category', 'due_date', 'completed']
    orderable_fields=['title', 'category__name', 'due_date', 'completed']
    Model = Task
    Form = TaskForm

class ExtrasExampleView():
    def index(request):
        return redirect('add_task')
