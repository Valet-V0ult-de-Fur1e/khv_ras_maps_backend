from __future__ import unicode_literals

from django.db import models

from django.contrib.gis.db import models


class m_2019_List_Of_Fields(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    geom = models.MultiPolygonField()
    reestr_number = models.CharField(blank=True, null=True, max_length=500)
    comment = models.CharField(blank=True, null=True, max_length=500)
    intern_number = models.CharField(blank=True, null=True, max_length=500)
    id_district = models.IntegerField(blank=True, null=True)
    id_owner = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    id_type_usage_plan = models.IntegerField(blank=True, null=True)
    id_type_usage_fact = models.IntegerField(blank=True, null=True)
    id_crop_plan = models.IntegerField(blank=True, null=True)
    id_crop_fact = models.IntegerField(blank=True, null=True)
    id_crop_sort_plan = models.IntegerField(blank=True, null=True)
    id_crop_sort_fact = models.IntegerField(blank=True, null=True)
    biochem_fact = models.CharField(blank=True, null=True, max_length=500)
    harvest_fact = models.FloatField(blank=True, null=True)
    harvest_forecast = models.FloatField(blank=True, null=True)
    pesticides = models.CharField(blank=True, null=True, max_length=500)
    fertilizers = models.CharField(blank=True, null=True, max_length=500)
    sowing_date = models.DateField(blank=True, null=True)
    harvesе_date = models.DateField(blank=True, null=True)
    inspected = models.BooleanField()
    hash_unique = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2019_list_of_fields'


class m_2022_List_Of_Fields(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    geom = models.MultiPolygonField()
    reestr_number = models.CharField(blank=True, null=True, max_length=500)
    comment = models.CharField(blank=True, null=True, max_length=500)
    intern_number = models.CharField(blank=True, null=True, max_length=500)
    id_district = models.IntegerField(blank=True, null=True)
    id_owner = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    id_type_usage_plan = models.IntegerField(blank=True, null=True)
    id_type_usage_fact = models.IntegerField(blank=True, null=True)
    id_crop_plan = models.IntegerField(blank=True, null=True)
    id_crop_fact = models.IntegerField(blank=True, null=True)
    id_crop_sort_plan = models.IntegerField(blank=True, null=True)
    id_crop_sort_fact = models.IntegerField(blank=True, null=True)
    biochem_fact = models.CharField(blank=True, null=True, max_length=500)
    harvest_fact = models.FloatField(blank=True, null=True)
    harvest_forecast = models.FloatField(blank=True, null=True)
    pesticides = models.CharField(blank=True, null=True, max_length=500)
    fertilizers = models.CharField(blank=True, null=True, max_length=500)
    sowing_date = models.DateField(blank=True, null=True)
    harvesе_date = models.DateField(blank=True, null=True)
    inspected = models.BooleanField()
    hash_unique = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2022_list_of_fields'
