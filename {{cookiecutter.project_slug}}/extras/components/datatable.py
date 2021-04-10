import math
from django.http import JsonResponse
from django.db.models import Q

class DataTable():

    @staticmethod
    def list_ajax(request, orderable_fields, search_fields, Model):
        _start = request.GET.get('start')
        _length = request.GET.get('length')
        _search = request.GET.get('search[value]')
        _order_by = request.GET.get('order[0][column]')
        _order_dir = request.GET.get('order[0][dir]')

        if _order_by:
            _order_by_field = orderable_fields[int(_order_by)]
        else:
            _order_by_field = orderable_fields[0]

        if _order_dir:
            _order_by_field_order = "" if _order_dir == 'asc' else "-"
        else:
            _order_by_field_order = ""

        filters = Q()
        for search_field in search_fields:
            filters |= Q(**{"%s__contains" % search_field: _search })

        resources = Model.objects.filter(filters).order_by(_order_by_field_order+_order_by_field)

        total = resources.count()

        if _start and _length:
            start = int(_start)
            length = int(_length)
            page = math.ceil(start / length) + 1
            per_page = length

            resources = resources[start:start + length]

        def replace_none_values(dictionary):
            for key in dictionary:
                if(dictionary[key] is None or dictionary[key] == "None"):
                    dictionary[key] = "--"
            return dictionary


        data = [replace_none_values(resource.to_dict_json()) for resource in resources]

        response = {
            'data': data,
            'page': page,
            'per_page': per_page,
            'recordsTotal': total,
            'recordsFiltered': total,
        }
        return JsonResponse(response)