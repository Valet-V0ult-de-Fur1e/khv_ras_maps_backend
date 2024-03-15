from django.views.generic.base import (TemplateView)
import json
from django.core.serializers import (serialize)
from django.http import JsonResponse
from markers.models import *
import json
from khv_ras_maps_backend.settings import N_OF_YEARS


def JoinListOfCropsToFields(fields_json: dict) -> dict:
    if type(fields_json) == str:
        fields_json = json.loads(fields_json)
    lst_of_crops_json = json.loads(serialize("geojson", ListOfCrops.objects.all().using("KhvDb")))
    lst_of_crops_dict = dict()

    # print(lst_of_crops_json["features"])

    for i in lst_of_crops_json["features"]:
        # print(i)
        lst_of_crops_dict[i["id"]] = i["properties"]

    for i in range(len(fields_json["features"])):
        # print(list(fields_json["features"][i]))
        if fields_json["features"][i]["properties"]["id_crop_fact"] == None:
            pass
        else:
            crop_data = lst_of_crops_dict[fields_json["features"][i]["properties"]["id_crop_fact"]]
            for row_key in crop_data:
                fields_json["features"][i]["properties"][row_key] = crop_data[row_key]
    return json.dumps(fields_json)



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
            JoinListOfCropsToFields(serialize(
                "geojson",
                y2019ListOfFields.objects.using('KhvDb').all(),
            ))
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
            JoinListOfCropsToFields(serialize(
                "geojson",
                y2019ListOfFields.objects.using('KhvDb').all(),
            ))
        )
        context["markers2022"] = json.loads(
            JoinListOfCropsToFields(serialize(
                "geojson",
                y2022ListOfFields.objects.using('KhvDb').all(),
            ))
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
        template_out = "context['markers{year}'] = json.loads(JoinListOfCropsToFields(serialize('geojson', y{year}ListOfFields.objects.using('KhvDb').all())))"
        for i in range(N_OF_YEARS):
            year = str(2019 + i)
            exec(template_out.format(year=year))
        return context
    

def index(request):
    context = {}
    template_out = "context['markers{year}'] = json.loads(JoinListOfCropsToFields(serialize('geojson', y{year}ListOfFields.objects.using('KhvDb').all())))"
    for i in range(N_OF_YEARS):
        year = str(2019 + i)
        exec(template_out.format(year=year))
    return JsonResponse(context)