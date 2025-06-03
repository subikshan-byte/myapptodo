from django.urls import path
from django.conf.urls import handler400
from . import views
app_name="todo"
handler404="views.f404"
urlpatterns = [
    path("home/",views.login_button,name="login_button"),
    path("login",views.login,name='login'),
    path("signup",views.signup,name='signup'),
    path("signupsuccess",views.signup_button,name='signup_button'),
    path("newtask",views.newtask,name="newtask"),
        path("home/newaskadded",views.newtask_button,name="task_button"),
        path("",views.index,name="index")
]
