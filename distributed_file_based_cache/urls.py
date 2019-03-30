from django.urls import include, path

urlpatterns = [
    path("serviceless_distributor", include("django_serviceless_distributor.urls"))
]
