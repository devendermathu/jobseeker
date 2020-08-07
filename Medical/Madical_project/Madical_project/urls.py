"""Madical_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from App_madical.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Homepage,name="Homepage"),
    # path('',orderpage),
    path('add/',addpage,name='add'),
    path('coming_data/',datapage,name='datapage'),
    path('see/<int:a>/',view_content_page,name='view_content_page'),
    path('addblock/',addpage,name='addpage'),
    path('update/<int:k>/',update_page,name='update_page'),
    path('upd/',update_page2,name='update_page2'),
    path('delete/<int:d>/',deletepage,name='deletepage'),
    path('enter_products/',product_page,name='product_page'),
    path('Product/',enter_product_page,name='enter_product_page'),
    path('updateData/',updateData_page,name='updateData_page'),
    path('find_update/',find_and_update,name='find_and_update'),
    path('report/',report_page,name='report_page'),
    path('get_report/',get_report_page,name='get_report_page')
]
