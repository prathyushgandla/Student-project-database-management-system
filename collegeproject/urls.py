from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.conf.urls import url

urlpatterns=[
    path('createproject',views.createProject,name="createproject"),
    path('register',views.register,name='register'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutPage,name='logout'),
    path('',views.home,name="home"),
    path('data/<str:id>/',views.data,name='data'),
    path('update/<str:id1>/',views.update,name='update'),
    path('delete/<str:id2>/',views.delete,name='delete'),
    path('search',views.search,name="search"),
    path('modifypage',views.updatePage,name="modifypage"),
    path('deleteitem/<str:id3>/',views.deleteItem,name='deleteitem'),
    path('uploadexcelfile',views.uploadfile, name='uploadexcelfile'),
    path('exportcsv',views.exportcsv,name='exportcsv')
]