from django.urls import path

from markers.views import MarkersMapView, MarkersMapViewTwoLayers, MarkersMapViewAllLayers, index

app_name = "markers"

urlpatterns = [
    path(
        "map/", MarkersMapView.as_view()
    ),
    path(
        "map2Layers/", MarkersMapViewTwoLayers.as_view()
    ),
    path(
        "mapAllLayers/", MarkersMapViewAllLayers.as_view()
    ),
    path(
        "getData/", index
    ),
]