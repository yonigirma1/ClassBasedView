from django.conf.urls import url

from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name = 'list'),
    url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name = 'detail')


]
