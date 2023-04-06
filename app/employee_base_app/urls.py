from django.urls import path
from .views import index, detail

urlpatterns = [
    path('', index, name='index'),
    path('<int:employee_id>', detail, name='detail')
]
