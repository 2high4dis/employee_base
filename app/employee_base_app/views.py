from django.shortcuts import render, get_object_or_404
from .models import Employee
from django.views.generic import ListView
from django.db.models import Q


def index(request):
    return render(request=request, template_name='employee_base_app/index.html')


def detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    context = {
        'employee': employee
    }
    return render(request=request, template_name='employee_base_app/detail.html', context=context)


class Search(ListView):
    model = Employee
    template_name = 'employee_base_app/search.html'

    def get_queryset(self):
        filter = self.request.GET.get('q')
        employees = Employee.objects.filter(Q(pk=int(filter)) if filter.isdigit() else (Q(pib__icontains=filter) | Q(post__icontains=filter) |
                                                                                        Q(email__icontains=filter) | Q(post__icontains=filter.replace(' ', '_'))))
        return employees
