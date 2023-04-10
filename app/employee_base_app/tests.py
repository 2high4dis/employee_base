import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Employee
from django.urls import reverse
from faker import Faker

fake = Faker()


def create_employee(name, weeks):
    time = timezone.now() + datetime.timedelta(weeks=weeks)
    return Employee.objects.create(pib=name, employ_date=time)


class EmployeeIndexViewTests(TestCase):
    def test_no_employees(self):
        responce = self.client.get(reverse('index'))
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, '')
        self.assertQuerysetEqual(responce.context['employees'], [])

    def test_old_employee(self):
        employee = create_employee(name=fake.name(), weeks=-5)
        responce = self.client.get(reverse('index'))
        self.assertQuerysetEqual(responce.context['employees'], [employee])

    def test_future_employee(self):
        create_employee(name=fake.name(), weeks=10)
        responce = self.client.get(reverse('index'))
        self.assertContains(responce, '')
        self.assertQuerysetEqual(responce.context['employees'], [])

    def test_future_and_old_employees(self):
        employee = create_employee(name=fake.name(), weeks=-10)
        create_employee(name=fake.name(), weeks=10)
        responce = self.client.get(reverse('index'))
        self.assertQuerysetEqual(responce.context['employees'], [employee])


class EmployeeDetailViewTests(TestCase):

    def test_future_employee(self):
        future_employee = create_employee(name=fake.name(), weeks=10)
        url = reverse('detail', args=(future_employee.id,))
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, 404)

    def test_old_employee(self):
        old_employee = create_employee(name=fake.name(), weeks=-5)
        url = reverse('detail', args=(old_employee.id,))
        responce = self.client.get(url)
        self.assertContains(responce, old_employee.pib)


class EmployeeModelTests(TestCase):

    def test_was_employeed_recently_with_future_employ_date(self):
        time = timezone.now() + datetime.timedelta(weeks=10)
        future_employee = Employee(employ_date=time)
        self.assertIs(future_employee.was_employeed_recently(), False)

    def test_was_employeed_recently_with_old_employ_date(self):
        time = timezone.now() - datetime.timedelta(weeks=15)
        old_employee = Employee(employ_date=time)
        self.assertIs(old_employee.was_employeed_recently(), False)

    def test_was_employeed_recently_with_current_employ_date(self):
        time = timezone.now()
        employee_with_current_employ_date = Employee(employ_date=time)
        self.assertIs(
            employee_with_current_employ_date.was_employeed_recently(), True)
