from django.contrib import admin
from django.urls import path
from canada import views
from canada.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/',views.contact_create),
    path('contact_all/',views.contact_list),
]
