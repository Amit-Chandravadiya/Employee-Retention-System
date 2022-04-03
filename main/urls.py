from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('services',views.service,name='services'),
    path('upload',views.upload,name='upload'),
    path('upload2',views.upload2,name='upload2')
]