from django.urls import path
from beckyShare import views

urlpatterns = [
    path('opsuser/', views.OpsUserView.as_view()),
    path('login/opsuser', views.OpsUserLogin.as_view()),
    path('client/signup/', views.ClientSignup.as_view()),
    path('client/Lists/', views.ClientListall.as_view()),
    path('client/download/<int:pk>', views.ClientFileDownload.as_view())
] 