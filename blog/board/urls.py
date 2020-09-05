"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.write_create, name="write_create"),
    path('read/', views.write_read, name="write_read"),
    path('read/<int:pk>', views.write_read_one, name="write_read_one"),
    path('update/<int:pk>', views.write_update, name="write_update"),
    path('delete/<int:pk>', views.write_delete, name="write_delete"),
]
