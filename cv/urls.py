from django.contrib import admin
from django.urls import path
from resume.views import index,fronts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('fronts/',fronts),
]
