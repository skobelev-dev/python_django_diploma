from django.urls import path
from rest_framework.reverse import reverse_lazy

app_name = "catalogapp"

url_for_products_ids = reverse_lazy(
        "catalogapp:get-products-ids"
    )

urlpatterns = []
