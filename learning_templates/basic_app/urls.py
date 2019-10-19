from django.urls import path, include
from basic_app import views

#FOR TEMPLATE TAGGING SET A GLOBAL NAME APP_ANME
app_name = 'basic_app'

#urlpatterns lists the html path can be shortened or extended.
urlpatterns= [
    path('basic_app/relative', views.relative, name='relative'),
    path('basic_app/other', views.other, name='other'),
    #path('basic_app/index', views.index, name='index'),
]

#urlpatterns=[
#    re_path(r'^relative/$',views.relative,name='relative'),
#    re_path(r'^other/$',views.other,name='other'),
#]
