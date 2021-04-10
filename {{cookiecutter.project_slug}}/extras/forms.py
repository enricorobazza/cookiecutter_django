from django import forms
from django.db import models
from django.urls import reverse_lazy

from extras.models import Task, Category
from extras.inputs.date import DateInput
from extras.widgets.insert import SelectAndInsert

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Nome"
        self.fields["description"].label = "Descrição"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'due_date': DateInput(format=('%Y-%m-%d')),
            'category': SelectAndInsert(title="Adicionar Categoria", form=CategoryForm, add_url=reverse_lazy('category_add_ajax'))
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["title"].label = "Título"
        self.fields["description"].label = "Descrição"
        self.fields["category"].label = "Categoria"
        self.fields["due_date"].label = "Data"
        self.fields["completed"].label = "Completa?"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields["category"].widget.attrs['class'] += ' selectpicker filter'