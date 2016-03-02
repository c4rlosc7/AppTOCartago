#url settings of transports

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^transports/', views.transports)
]

