from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sell", views.sellitem, name="sellitem"),
    path("category", views.category, name="category"),
    path("category/<str:catname>", views.speccat, name="speccat"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("item/<int:itemid>", views.itemize, name="itemize")
]
