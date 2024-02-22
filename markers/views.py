from django.views.generic.base import (
    TemplateView,
)
import json

from django.core.serializers import (
    serialize,
)

from markers.models import *
import json

class MarkersMapView(TemplateView):
    template_name = "map.html"

    def get_context_data(
        self, **kwargs
    ):
        context = (
            super().get_context_data(
                **kwargs
            )
        )
        context["markers"] = json.loads(
            serialize(
                "geojson",
                y2019ListOfFields.objects.using('khvDB').all(),
            )
        )
        return context
    

class MarkersMapViewTwoLayers(TemplateView):
    template_name = "twoLayers.html"

    def get_context_data(
        self, **kwargs
    ):
        context = (
            super().get_context_data(
                **kwargs
            )
        )
        context["markers2019"] = json.loads(
            serialize(
                "geojson",
                y2019ListOfFields.objects.using('khvDB').all(),
            )
        )
        context["markers2022"] = json.loads(
            serialize(
                "geojson",
                y2022ListOfFields.objects.using('khvDB2').all(),
            )
        )
        return context