"""myWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myHome import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
	path('index/', views.index, name='index'),
	path('login/',views.login, name='login'),
	path('logout/',views.logout, name='logout'),
	path('signup/',views.signup, name='signup'),
	path('list/',views.list, name='list'),
	path('inspectionlist/',views.inspectionlist, name='inspectionlist'),
	path('addfireextinguisher/',views.addfireextinguisher, name='addfireextinguisher'),
	path('updatefireextinguisher/',views.updatefireextinguisher, name='updatefireextinguisher'),
	path('userlist/', views.userlist, name='userlist'),	
	path('updateuser/', views.updateuser, name='updateuser'),
	path('activeuser/', views.activeuser, name='activeuser'),
	path('deleteuser/', views.deleteuser, name='deleteuser'),
	path('qrreader/',views.qrreader, name='qrreader'),
	path('qrapi/',views.qrapi, name='qrapi'),
	path('updateinspectiondate/<int:pk>',views.updateinspectiondate, name='updateinspectiondate'),
]

urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
