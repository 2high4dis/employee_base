from django.urls import path
from .views import IndexView, DetailView, Search, register, profile, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView
from django.contrib.auth import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>', DetailView.as_view(), name='detail'),
    path('search/', Search.as_view(), name='search'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('<int:pk>/update', EmployeeUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='delete'),
    path('create/', EmployeeCreateView.as_view(), name='create')
]
