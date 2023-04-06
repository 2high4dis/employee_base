from django.shortcuts import render, get_object_or_404
from .models import Employee


def index(request):
    return render(request=request, template_name='employee_base_app/index.html')


def detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    context = {
        'employee': employee
    }
    return render(request=request, template_name='employee_base_app/detail.html', context=context)
