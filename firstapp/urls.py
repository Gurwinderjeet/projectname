from firstapp import views
from django.conf.urls import url

app_name="firstapp"
urlpatterns = [
    url(r'^index/$', views.userhome),
    url(r'^addroles/$', views.addroles),
    url(r'^excluderole/$', views.excluderole)

]
