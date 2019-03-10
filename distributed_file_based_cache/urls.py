from django.urls import include, path

urlpatterns = [path("serviceless_distributor", include("serviceless_distributor.urls"))]
