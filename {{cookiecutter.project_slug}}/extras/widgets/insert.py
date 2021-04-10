from django.forms.widgets import Select
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

def set_fields_not_required(fields):
    for field in fields:
        fields[field].required = False
class SelectAndInsert(Select):
    template_name = 'extras/widgets/insert_widget.html'

    def __init__(self, attrs=None, title=None, form=None, add_url=None):
        super(SelectAndInsert, self).__init__()
        self.title = title
        self.form = form
        self.add_url = add_url

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['title'] = self.title
        context['widget']['add_url'] = self.add_url
        if(self.form is not None):
            form = self.form(prefix=name+"_form")
            set_fields_not_required(form.fields)
            context['widget']['form'] = form
        return context