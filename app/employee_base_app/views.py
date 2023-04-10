from django.shortcuts import render, redirect
from .models import Employee
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterForm


class IndexView(ListView):
    template_name = 'employee_base_app/index.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return Employee.objects.filter(employ_date__lte=timezone.now()).select_related('pib', 'post', 'id', 'parent_id').prefetch_related('employee__parent', 'parent__pib', 'parent__post')


class DetailView(DetailView):
    model = Employee
    template_name = 'employee_base_app/detail.html'

    def get_queryset(self):
        return Employee.objects.filter(employ_date__lte=timezone.now())


class Search(ListView):
    model = Employee
    template_name = 'employee_base_app/search.html'

    def get_queryset(self):
        filter = self.request.GET.get('q')
        employees = Employee.objects.filter(employ_date__lte=timezone.now()).filter(Q(pk=int(filter)) if filter.isdigit() else (Q(pib__icontains=filter) | Q(post__icontains=filter) |
                                                                                                                                Q(email__icontains=filter) | Q(post__icontains=filter.replace(' ', '_'))))
        return employees


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account {username} created!')
            return redirect('login')
        else:
            form = UserRegisterForm()
            return render(request=request, template_name='registration/registration.html', context={'form': form})
    else:
        form = UserRegisterForm()
        return render(request=request, template_name='registration/registration.html', context={'form': form})


@login_required
def profile(request):
    return render(request, template_name='registration/profile.html')


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    fields = ['pib', 'employ_date', 'post', 'email', 'parent']
    template_name = 'employee_base_app/employee_form.html'


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = ['pib', 'employ_date', 'post', 'email', 'parent']
    template_name = 'employee_base_app/employee_form.html'


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'employee_base_app/delete_confirmation.html'
    success_url = '/'
