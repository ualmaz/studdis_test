from django.contrib import admin
from django.urls import path
from studdis import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/students/$', views.students_list),
    url(r'^api/students/(?P<pk>[0-9]+)$', views.students_detail),
]
