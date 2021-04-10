from django.urls import path{% if cookiecutter.extras_example == "True" %}, include{% endif %}
from main.views.index import IndexView

urlpatterns = [
    path('', IndexView.index, name='index'),
    {% if cookiecutter.extras_example == "True" %}path('extras/', include('extras.urls')),{% endif %}
]