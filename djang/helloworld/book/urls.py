from django.urls import path,include
from  django.urls import path,re_path,include
from django.contrib import admin
from . import views
from django.contrib.auth import  views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
     path("index/",views.index),
     path("add/",views.add),
    path("edit/",views.edit),
     path("delete/",views.delete),
    path("accounts/",include('django.contrib.auth.urls')),
    path('accounts/profile/', views.index),
    # path('accounts/login/',views.login),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/login_out2.html'),name='logout2'),
    path("",views.login1)
    # 映射自定义的视图
    # path("accounts/login",views.login)


]