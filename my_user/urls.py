from django.urls import path
from my_user import views

urlpatterns = [path('', views.index, name='home'),
               path('invalid_login/', views.invalid_loginView,
                    name='invalid_login'),
               path('login/', views.login, name='login')]
