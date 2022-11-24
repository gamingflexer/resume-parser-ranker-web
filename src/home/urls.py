from . import views
from django.urls import path

urlpatterns = [     
    #<--------- Authentication releted path / urls start here ------->
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.Auth.sign_out,name='sign_out'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('upload',views.upload,name='upload'),
    path('comingsoon',views.page_404,name='404'),
    path('profile',views.profile,name='profile'),
    path('forgetpassword',views.forget_password,name='forget_password'),
    path('mail_recevied',views.mail_recevied,name='mail_recevied'),
    
    #<--------- other path / urls end here ------->
    path('', views.index, name='home'),
    ]

#path('',views.rawData, name='rawData')