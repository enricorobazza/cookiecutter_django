from django.urls import path
from main.views.index import IndexView
from extras.views.example import TaskView, CategoryView, ExtrasExampleView

urlpatterns = [
    path('', ExtrasExampleView.index, name="extras_index"),
    path('task/', TaskView.as_view()),
    path('category/add-ajax', CategoryView.add_ajax, name='category_add_ajax')
]