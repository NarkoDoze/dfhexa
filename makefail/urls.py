from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^makefail$', views.make_fail, name='home'),
]