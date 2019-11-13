from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", app.views.home, name="home"),
    path(
        "dog-product/<dog_product_id>",
        app.views.dog_product_detail,
        name="dog_product_detail",
    ),
    path(
        "dog-product/<dog_product_id>/purchase",
        app.views.purchase_dog_product,
        name="purchase_dog_product",
    ),
    path("purchase_dog_product", app.views.purchase_detail, name="purchase_detail"),
    path("dogtag/new", app.views.new_dog_tag, name="new_dog_tag"),
    path("dogtag", app.views.dog_tag_list, name="dog_tag_list"),
]
