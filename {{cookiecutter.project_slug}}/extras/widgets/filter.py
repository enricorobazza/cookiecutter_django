from django.forms.widgets import Select
import json


class Filter(Select):
    template_name = 'extras/widgets/filter_widget.html'

    def __init__(self, attrs=None, queryset=None, field=None):
        super(Filter, self).__init__()
        self.field = field
        self.queryset = queryset

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['field'] = self.field
        context['widget']['queryset'] =  json.dumps([obj.as_dict_for_filter() for obj in self.queryset ])
        return context