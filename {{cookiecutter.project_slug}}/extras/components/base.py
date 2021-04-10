
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path as _path, include
from extras.components import DataTable

def get_verbose_name(Model):
    return Model._meta.verbose_name.replace(" ", "_")

class BaseView():
    add_urls = {}
    list_url = ""
    list_ajax_url = ""
    add_url = ""
    delete_url = ""
    edit_url = ""
    verbose_name = ""
    verbose_name_plural = ""
    methods = ['list', 'add', 'delete', 'edit', 'list-ajax']
    search_fields = []
    orderable_fields = []

    @classmethod
    def url(cls, path, name, Model):
        def inner(func):
            verbose_name = get_verbose_name(Model)
            if verbose_name in cls.add_urls:
                cls.add_urls[verbose_name].append({"path": path, "name": name, "func": func})
            else:
                cls.add_urls[verbose_name] = [{"path": path, "name": name, "func": func}]
        return inner

    @classmethod
    def as_view(cls):
        obj = cls()
        return obj.urls()

    def urls(self):
        self.verbose_name = get_verbose_name(self.Model)
        self.verbose_name_plural = self.Model._meta.verbose_name_plural

        self.list_url = self.verbose_name_plural
        self.list_ajax_url = "list_ajax_%s"%self.verbose_name
        self.add_url = "add_%s"%self.verbose_name
        self.delete_url = "delete_%s"%self.verbose_name
        self.edit_url = "edit_%s"%self.verbose_name

        urls = []
        if('list' in self.methods):
            urls += [_path('', self.list, name=self.list_url)]
        if('list-ajax' in self.methods):
            urls += [_path('list-ajax/', self.list_ajax, name=self.list_ajax_url)]
        if('add' in self.methods):
            urls += [_path('add/', self.add, name=self.add_url)]
        if('delete' in self.methods):
            urls += [_path('<int:pk>/delete/', self.delete, name=self.delete_url)]
        if('edit' in self.methods):
            urls += [_path('<int:pk>/', self.edit, name=self.edit_url)]

        if self.verbose_name in self.add_urls:
            for url in self.add_urls[self.verbose_name]:
                urls += [_path(url["path"], url["func"] , name=url["name"])]
        
        return include(urls)

    def list(self, request):
        if('list-ajax' in self.methods):
            resources = list()
        else:
            resources = self.Model.objects.all()
        edit_url = self.edit_url if 'edit' in self.methods else ""
        delete_url = self.delete_url if 'delete' in self.methods else ""
        add_url = self.add_url if 'add' in self.methods else ""
        list_url = self.list_ajax_url if 'list-ajax' in self.methods else ""

        table_fields = json.dumps(self.table_fields + ['pk'])
        template_path = self.template_path
        
        return render(request, template_path + '/list.html', {
            'resources': resources, 'edit_url': edit_url, 'delete_url': delete_url,
            'list_url': list_url, 'add_url': add_url,
            'table_fields': table_fields
        })
    
    def list_ajax(self, request):
        orderable_fields = self.orderable_fields
        search_fields = orderable_fields if len(self.search_fields) == 0 else self.search_fields
        return DataTable.list_ajax(request, orderable_fields, search_fields, self.Model)

    def add(self, request):
        full_template_path = self.template_path + '/add.html'
        if request.method == 'POST':

            form = self.Form(request.POST)

            if form.is_valid():
                form.save()

                return redirect(self.list_url)
            else:
                return render(request, full_template_path, {'form': form })
        else:
            form = self.Form()
            return render(request, full_template_path, {'form': form})

    def edit(self, request, pk):
        full_template_path = self.template_path + '/edit.html'
        resource = get_object_or_404(self.Model, pk=pk)
        if(request.method == 'POST'):
            form = self.Form(request.POST, instance=resource)

            if(form.is_valid()):
                resource = form.save()
                return redirect(self.list_url)
            else:
                return render(request, full_template_path, {'form': form})
        else:
            form = self.Form(instance=resource)
            return render(request, full_template_path, {'form': form})

    def delete(self, request, pk):
        # if(not request.user.is_staff):
            # return redirect(self.list_url)

        self.Model.objects.get(pk=pk).delete()
        return redirect(self.list_url)