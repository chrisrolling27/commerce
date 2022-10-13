from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing


def index(request):
    return render(request, "auctions/index.html", {
    "listings": Listing.objects.all()
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def sellitem(request):
    return render(request, "auctions/sellitem.html")

def watchlist(request):
    return render(request, "auctions/watchlist.html")

def category(request):
    cat = Listing.objects.order_by().values_list('category', flat=True).distinct()
    return render(request, "auctions/category.html", {
    "dist_categories": cat
    })

def speccat(request, catname):
    catreturn = Listing.objects.filter(category=catname)
    return render(request, "auctions/specific_category.html", {
    "catreturn": catreturn, "catname" : catname
    })

def itemize(request, itemid):
    thingy = Listing.objects.get(id=itemid)
    return render(request, "auctions/itemize.html", {
    "thingy" : thingy
    })
