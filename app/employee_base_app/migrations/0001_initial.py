# Generated by Django 4.2 on 2023-04-06 12:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pib', models.CharField(max_length=100)),
                ('post', models.CharField(choices=[('ceo', 'CEO'), ('deputy_ceo', 'Deputy CEO'), ('regional_manager', 'Regional Manager'), ('territorial_manager', 'Territorial Manager'), ('deputy_territorial_manager', 'Deputy Territorial Manager'), ('head_of_network', 'Head of Network'), ('pharmacist', 'Pharmacist')], default='pharmacist', max_length=50)),
                ('employ_date', models.DateField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=100)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('boss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_base_app.employee', verbose_name='Boss')),
            ],
        ),
    ]
