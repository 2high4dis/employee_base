from django.urls import path
from .views import index, detail, Search

urlpatterns = [
    path('', index, name='index'),
    path('<int:employee_id>', detail, name='detail'),
    path('search/', Search.as_view(), name='search')
]
