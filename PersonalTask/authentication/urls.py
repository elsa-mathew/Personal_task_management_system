from django.urls import path
from . import views

urlpatterns = [
    path(".",views.home,name="home"),
    path("register/",views.register,name="register"),
    path("",views.login_page,name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout_view, name="logout"),
    path(
    "change-password/",
    views.change_password,
    name="change_password"
),

]