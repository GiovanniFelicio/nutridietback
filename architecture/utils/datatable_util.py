from django.db.models import Q
from architecture.utils.object_util import ObjectUtil


class DataTableUtil:

    @classmethod
    def query_datatable(cls, queryset, vo, serializer, request_data):

        draw = request_data['draw']
        length = request_data['length']
        start = request_data['start']
        search_value = request_data['search']
        order = request_data['order']
        order_column = 0
        order_mode = 'desc'

        if ObjectUtil.is_not_none(order):
            order_column = order[0]['column']
            order_mode = order[0]['dir']

        values_vo = vo.get_values()

        order_column = values_vo[order_column].name

        if order_mode == 'desc':
            order_column = '-' + order_column

        total = queryset.count()

        if search_value['value'] != '':
            or_condition = cls.__get_condition_q(values_vo, search_value, Q.OR)

            queryset = queryset.filter(or_condition)

        count = queryset.count()
        queryset = queryset.order_by(order_column)[start:start + length]

        data = serializer(queryset, many=True)

        return {
            'data': data.data,
            'recordsFiltered': count,
            'recordsTotal': total,
            'draw': draw
        }

    @classmethod
    def __get_columns_label(cls, values_vo):
        labels = []
        for value_vo in values_vo:
            labels.append(value_vo.label)

        return labels

    @classmethod
    def __get_condition_q(cls, values_vo, search_value, condition) -> Q:
        or_condition = Q()

        for value_vo in values_vo:
            key = value_vo.name + '__icontains'
            field = {key: search_value['value']}
            or_condition.add(Q(**field), condition)

        return or_condition

    # {'draw': 1, 'columns': [{'data': 'name', 'name': '', 'searchable': True, 'orderable': True, 'search': {'value': '', 'regex': False}}, {'data': 'document', 'name': '', 'searchable': True, 'orderable': True, 'search': {'value': '', 'regex': False}}], 'order': [{'column': 0, 'dir': 'asc'}], 'start': 0, 'length': 10, 'search': {'value': '', 'regex': False}}
