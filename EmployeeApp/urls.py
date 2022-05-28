from django.urls import re_path
from EmployeeApp import views


urlpatterns = [
    re_path(r'^department$', views.DepartmentApi),
    re_path(r'^department/([0-9]+)$', views.DepartmentApi)
]
