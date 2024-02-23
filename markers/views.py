from django.views.generic.base import (TemplateView)
import json
from django.core.serializers import (serialize)
from markers.models import *
import json
from khv_ras_maps_backend.settings import N_OF_YEARS

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
                y2019ListOfFields.objects.using('KhvDB2019').all(),
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
                y2019ListOfFields.objects.using('KhvDb2019').all(),
            )
        )
        context["markers2022"] = json.loads(
            serialize(
                "geojson",
                y2022ListOfFields.objects.using('KhvDb2022').all(),
            )
        )
        return context


class MarkersMapViewAllLayers(TemplateView):
    template_name = "allLayers.html"

    def get_context_data(self, **kwargs):
        context = (
            super().get_context_data(
                **kwargs
            )
        )
        context["markers2019"] = json.loads(
            serialize(
                "geojson",
                y2019ListOfFields.objects.using('KhvDb2019').all(),
            )
        )
        context["markers2022"] = json.loads(
            serialize(
                "geojson",
                y2022ListOfFields.objects.using('KhvDb2022').all(),
            )
        )
        return context