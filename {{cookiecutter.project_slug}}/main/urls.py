from django.urls import path
from main.views.index import IndexView

urlpatterns = [
    path('', IndexView.index, name='index'),
]