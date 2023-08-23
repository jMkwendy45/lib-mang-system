from django_filters import FilterSet
from .models import Book


class CustomFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'author_id': ['exact'],
            'title': ['exact'],
            'total_copies_brought': ['gt', 'lt']
        }
