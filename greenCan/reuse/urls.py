from django.urls import path

from . import views

app_name = "reuse"

urlpatterns = [
    path("", views.index, name="index"),
    path("donations/", views.donation_view, name="donation-page"),
    path("listings/", views.listing_page, name="listing-page"),
    path("create_post/", views.create_post, name="create-post"),
]
