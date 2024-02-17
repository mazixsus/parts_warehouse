from rest_framework import filters

class CategoriesFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name')
        parent = request.query_params.get('parent')

        if name:
            queryset = queryset.filter(name=name)

        if parent:
            queryset = queryset.filter(parent=parent)

        return queryset