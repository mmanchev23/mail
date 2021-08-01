from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_view, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),

    # API Routes
    path("emails", views.compose_view, name="compose"),
    path("emails/<int:email_id>", views.email_view, name="email"),
    path("emails/<str:mailbox>", views.mailbox_view, name="mailbox"),
]
