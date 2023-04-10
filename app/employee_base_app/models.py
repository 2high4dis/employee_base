from django.db import models
import mptt
import datetime
from django.utils import timezone
from django.urls import reverse

choices = (
    ('ceo', 'CEO'),
    ('deputy_ceo', 'Deputy CEO'),
    ('regional_manager', 'Regional Manager'),
    ('territorial_manager', 'Territorial Manager'),
    ('deputy_territorial_manager', 'Deputy Territorial Manager'),
    ('head_of_network', 'Head of Network'),
    ('pharmacist', 'Pharmacist')
)

posts = {
    'ceo': 'CEO',
    'deputy_ceo': 'Deputy CEO',
    'regional_manager': 'Regional Manager',
    'territorial_manager': 'Territorial Manager',
    'deputy_territorial_manager': 'Deputy Territorial Manager',
    'head_of_network': 'Head of Network',
    'pharmacist': 'Pharmacist'
}


class Employee(models.Model):
    pib = models.CharField(max_length=100)
    post = models.CharField(
        max_length=50, choices=choices, default='pharmacist')
    employ_date = models.DateField(default=timezone.now)
    email = models.EmailField(max_length=100)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Boss')

    def __str__(self):
        return f'{self.pib} ({self.post})'

    def get_post(self):
        return posts[f'{self.post}']

    def was_employeed_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(weeks=10) <= self.employ_date <= now

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


mptt.register(Employee)
