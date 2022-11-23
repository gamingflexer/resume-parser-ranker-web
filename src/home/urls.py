from . import views
from django.urls import path

urlpatterns = [     
    #<--------- Authentication releted path / urls start here ------->
    path('sign_up',views.Auth.sign_up,name='sign_up'),
    path('sign_in',views.Auth.sign_in,name='sign_in'),
    path('sign_out',views.Auth.sign_out,name='sign_out'),
    
    #<--------- other path / urls end here ------->
    path('', views.index, name='home'),
    ]

#path('',views.rawData, name='rawData')