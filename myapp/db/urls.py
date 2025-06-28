from django .urls import path
from . import views

app_name = 'db'
urlpatterns = [
    path('index', views.index, name='index'),# type: ignore
    path('aboutus',views.aboutus, name='aboutus'),# type: ignore
    path('register',views.register, name="register"),# type: ignore
    path('login',views.login, name="login"),# type: ignore
    path('contact',views.contact, name="contact"),# type: ignore
    path("dashboard", views.dashboard, name="dashboard"),# type: ignore
    path('detail/<int:post_id>', views.detail, name='detail'),# type: ignore
    path('logout', views.logout,name= 'logout'), # type: ignore 
    path('forgot_password',views.forgot_password, name='forgot_password'), # type: ignore
    path('reset-password/<uidb64>/<token>/',views.reset_password,name='reset_password'), # type: ignore
    path('edit_profile',views.edit_profile, name='edit_profile')
]
