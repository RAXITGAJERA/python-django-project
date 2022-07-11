from django.urls import path, include
from raxit import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('edituser(?p<id>[0-9]+)',views.edituser, name='edituser'),
    path('updateuser', views.updateuser, name='updateuser'),

    path('homeadmin', views.homeadmin, name='homeadminpage'),

    path('loginuser', views.loginuser, name='loginuserpage'),
    path('signupuser', views.signupuser, name='signupuserpage'),
    path('logout', views.logoutuser,name='logoutpage'),
    
    path('loginadmin', views.loginadmin, name='loginadminpage'),

    path('addvideo', views.addvideo, name='addvideopage'),
    path('edvideo(?p<id>[0-9]+)',views.editvideo, name='editvideopage'),
    path('updatevideo', views.updatevideo, name='updatevideopage'),
    path('deletevideo(?p<id>[0-9]+)',views.deletevideo, name='deletevideopage'),

    path('addcoments(?p<id>[0-9]+)', views.addcoments, name='addcomentspage'),
    path('videocomments', views.videocomments, name='videocomments'),
    path('showcomments(?p<id>[0-9]+)', views.showcomments, name='showcomments'),

    path('homeuseradmin', views.homeuseradmin, name='homeuseradminpage'),
    path('eduser(?p<id>[0-9]+)',views.edituseradmin, name='edituseradmin'),
    path('updateuseradmin', views.updateuseradmin, name='updateuseradmin'),
    path('deleteuser(?p<id>[0-9]+)',views.deleteuseradmin, name='deleteuseradmin'),
    path('adduserbyadmin', views.adduserbyadmin, name='adduserbyadmin'),

]