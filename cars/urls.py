from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MainPage.as_view(), name='Main_page'),
    url(r'^new_car/$', views.AddNewCar.as_view(), name='Add_new_car'),
    url(r'^create_pdf/$', views.some_view, name='Pdf_creation')
]
