from . import views
from django.urls import path

urlpatterns = [     
    #<--------- Authentication releted path / urls start here ------->
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    # path('signup',views.signup,name='signup'),
    # path('signin',views.signin,name='signin'),
    # path('signout',views.Auth.sign_out,name='sign_out'),
    path('comingsoon',views.page_404,name='page_404'),
    path('upload',views.upload,name='upload'),
    path('profile',views.profile,name='profile'),
    # path('forgetpassword',views.forget_password,name='forget_password'),
    # path('mail_recevied',views.mail_recevied,name='mail_recevied'),
    
    #<-------- other path / urls end here ------->
    path('dashboard', views.dashboard, name='home'),
    path('', views.index, name='index'),
    
    ]

#path('',views.rawData, name='rawData')