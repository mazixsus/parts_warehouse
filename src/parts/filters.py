from rest_framework import filters

class PartsFilterBackend(filters.BaseFilterBackend):    
    part_fields = ['serial_number', 'name', 'description', 'category', 'quantity', 'price', 'location_option']

    def filter_queryset(self, request, queryset, view):
        
        for field in self.part_fields:
            field_value = request.query_params.get(field)

            if field_value:
                queryset = queryset.filter(**{field:field_value})

        return queryset