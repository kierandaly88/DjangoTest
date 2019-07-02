# from django.conf.urls import urls
# from . import views

# urlpatterns = [
#     url(r'^$', views.index, name='index')
# ]

from django.urls import path, re_path

from . import views

urlpatterns = [

  path('', views.index, name='index'),
  path('details/<int:id>/', views.details, name='details')
  # re_path(r'details/(?P<id>[0-9]+)/$', views.details, name='details')

  # re_path('details/(?P<id>)/$', views.details, name='details')
]


