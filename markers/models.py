from __future__ import unicode_literals

from django.db import models

from django.contrib.gis.db import models


class y2019ListOfFields(models.Model):
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


# class y2019Evi_20_1(models.Model):
#     db_table = '2019_EVI_20_1'
#     geom = models.PointField(blank=True, null=True)
#     x = models.FloatField(db_column='X')  # Field name made lowercase.
#     y = models.FloatField(db_column='Y')  # Field name made lowercase.
#     evi1 = models.FloatField(db_column='EVI1')  # Field name made lowercase.
#     evi2 = models.FloatField(db_column='EVI2')  # Field name made lowercase.
#     evi3 = models.FloatField(db_column='EVI3')  # Field name made lowercase.
#     evi4 = models.FloatField(db_column='EVI4')  # Field name made lowercase.
#     evi5 = models.FloatField(db_column='EVI5')  # Field name made lowercase.
#     evi6 = models.FloatField(db_column='EVI6')  # Field name made lowercase.
#     evi7 = models.FloatField(db_column='EVI7')  # Field name made lowercase.
#     evi8 = models.FloatField(db_column='EVI8')  # Field name made lowercase.
#     evi9 = models.FloatField(db_column='EVI9')  # Field name made lowercase.
#     evi10 = models.FloatField(db_column='EVI10')  # Field name made lowercase.
#     evi11 = models.FloatField(db_column='EVI11')  # Field name made lowercase.
#     evi12 = models.FloatField(db_column='EVI12')  # Field name made lowercase.
#     evi13 = models.FloatField(db_column='EVI13')  # Field name made lowercase.
#     evi14 = models.FloatField(db_column='EVI14')  # Field name made lowercase.
#     evi15 = models.FloatField(db_column='EVI15')  # Field name made lowercase.
#     evi16 = models.FloatField(db_column='EVI16')  # Field name made lowercase.
#     evi17 = models.FloatField(db_column='EVI17')  # Field name made lowercase.
#     evi18 = models.FloatField(db_column='EVI18')  # Field name made lowercase.
#     evi19 = models.FloatField(db_column='EVI19')  # Field name made lowercase.
#     evi20 = models.FloatField(db_column='EVI20')  # Field name made lowercase.
#     evi21 = models.FloatField(db_column='EVI21')  # Field name made lowercase.
#     evi22 = models.FloatField(db_column='EVI22')  # Field name made lowercase.
#     evi23 = models.FloatField(db_column='EVI23')  # Field name made lowercase.
#     evi24 = models.FloatField(db_column='EVI24')  # Field name made lowercase.
#     evi25 = models.FloatField(db_column='EVI25')  # Field name made lowercase.
#     evi26 = models.FloatField(db_column='EVI26')  # Field name made lowercase.
#     evi27 = models.FloatField(db_column='EVI27')  # Field name made lowercase.
#     evi28 = models.FloatField(db_column='EVI28')  # Field name made lowercase.
#     evi29 = models.FloatField(db_column='EVI29')  # Field name made lowercase.
#     evi30 = models.FloatField(db_column='EVI30')  # Field name made lowercase.
#     evi31 = models.FloatField(db_column='EVI31')  # Field name made lowercase.
#     evi32 = models.FloatField(db_column='EVI32')  # Field name made lowercase.
#     evi33 = models.FloatField(db_column='EVI33')  # Field name made lowercase.
#     evi34 = models.FloatField(db_column='EVI34')  # Field name made lowercase.
#     evi35 = models.FloatField(db_column='EVI35')  # Field name made lowercase.
#     evi36 = models.FloatField(db_column='EVI36')  # Field name made lowercase.
#     evi37 = models.FloatField(db_column='EVI37')  # Field name made lowercase.
#     evi38 = models.FloatField(db_column='EVI38')  # Field name made lowercase.
#     evi39 = models.FloatField(db_column='EVI39')  # Field name made lowercase.
#     evi40 = models.FloatField(db_column='EVI40')  # Field name made lowercase.
#     evi41 = models.FloatField(db_column='EVI41')  # Field name made lowercase.
#     evi42 = models.FloatField(db_column='EVI42')  # Field name made lowercase.
#     evi43 = models.FloatField(db_column='EVI43')  # Field name made lowercase.
#     evi44 = models.FloatField(db_column='EVI44')  # Field name made lowercase.
#     evi45 = models.FloatField(db_column='EVI45')  # Field name made lowercase.
#     evi46 = models.FloatField(db_column='EVI46')  # Field name made lowercase.
#     evi47 = models.FloatField(db_column='EVI47')  # Field name made lowercase.
#     evi48 = models.FloatField(db_column='EVI48')  # Field name made lowercase.
#     evi49 = models.FloatField(db_column='EVI49')  # Field name made lowercase.
#     evi50 = models.FloatField(db_column='EVI50')  # Field name made lowercase.
#     evi51 = models.FloatField(db_column='EVI51')  # Field name made lowercase.
#     evi52 = models.FloatField(db_column='EVI52')  # Field name made lowercase.
#     id_crop_plan = models.IntegerField(blank=True, null=True)
#     id_crop_pixel_result = models.IntegerField(blank=True, null=True)
#     id_field = models.ForeignKey(y2019ListOfFields, models.DO_NOTHING, db_column='id_field')
#     comment = models.CharField(blank=True, null=True, max_length=64)

#     class Meta:
#         managed = False
#         db_table = '2019_EVI_20_1'
#         unique_together = (('x', 'y'))


# class y2019Ndvi_10_1(models.Model):
#     geom = models.PointField(blank=True, null=True)
#     x = models.FloatField(db_column='X')  # Field name made lowercase.
#     y = models.FloatField(db_column='Y')  # Field name made lowercase.
#     ndv1 = models.FloatField(db_column='NDV1')  # Field name made lowercase.
#     ndv2 = models.FloatField(db_column='NDV2')  # Field name made lowercase.
#     ndv3 = models.FloatField(db_column='NDV3')  # Field name made lowercase.
#     ndv4 = models.FloatField(db_column='NDV4')  # Field name made lowercase.
#     ndv5 = models.FloatField(db_column='NDV5')  # Field name made lowercase.
#     ndv6 = models.FloatField(db_column='NDV6')  # Field name made lowercase.
#     ndv7 = models.FloatField(db_column='NDV7')  # Field name made lowercase.
#     ndv8 = models.FloatField(db_column='NDV8')  # Field name made lowercase.
#     ndv9 = models.FloatField(db_column='NDV9')  # Field name made lowercase.
#     ndv10 = models.FloatField(db_column='NDV10')  # Field name made lowercase.
#     ndv11 = models.FloatField(db_column='NDV11')  # Field name made lowercase.
#     ndv12 = models.FloatField(db_column='NDV12')  # Field name made lowercase.
#     ndv13 = models.FloatField(db_column='NDV13')  # Field name made lowercase.
#     ndv14 = models.FloatField(db_column='NDV14')  # Field name made lowercase.
#     ndv15 = models.FloatField(db_column='NDV15')  # Field name made lowercase.
#     ndv16 = models.FloatField(db_column='NDV16')  # Field name made lowercase.
#     ndv17 = models.FloatField(db_column='NDV17')  # Field name made lowercase.
#     ndv18 = models.FloatField(db_column='NDV18')  # Field name made lowercase.
#     ndv19 = models.FloatField(db_column='NDV19')  # Field name made lowercase.
#     ndv20 = models.FloatField(db_column='NDV20')  # Field name made lowercase.
#     ndv21 = models.FloatField(db_column='NDV21')  # Field name made lowercase.
#     ndv22 = models.FloatField(db_column='NDV22')  # Field name made lowercase.
#     ndv23 = models.FloatField(db_column='NDV23')  # Field name made lowercase.
#     ndv24 = models.FloatField(db_column='NDV24')  # Field name made lowercase.
#     ndv25 = models.FloatField(db_column='NDV25')  # Field name made lowercase.
#     ndv26 = models.FloatField(db_column='NDV26')  # Field name made lowercase.
#     ndv27 = models.FloatField(db_column='NDV27')  # Field name made lowercase.
#     ndv28 = models.FloatField(db_column='NDV28')  # Field name made lowercase.
#     ndv29 = models.FloatField(db_column='NDV29')  # Field name made lowercase.
#     ndv30 = models.FloatField(db_column='NDV30')  # Field name made lowercase.
#     ndv31 = models.FloatField(db_column='NDV31')  # Field name made lowercase.
#     ndv32 = models.FloatField(db_column='NDV32')  # Field name made lowercase.
#     ndv33 = models.FloatField(db_column='NDV33')  # Field name made lowercase.
#     ndv34 = models.FloatField(db_column='NDV34')  # Field name made lowercase.
#     ndv35 = models.FloatField(db_column='NDV35')  # Field name made lowercase.
#     ndv36 = models.FloatField(db_column='NDV36')  # Field name made lowercase.
#     ndv37 = models.FloatField(db_column='NDV37')  # Field name made lowercase.
#     ndv38 = models.FloatField(db_column='NDV38')  # Field name made lowercase.
#     ndv39 = models.FloatField(db_column='NDV39')  # Field name made lowercase.
#     ndv40 = models.FloatField(db_column='NDV40')  # Field name made lowercase.
#     ndv41 = models.FloatField(db_column='NDV41')  # Field name made lowercase.
#     ndv42 = models.FloatField(db_column='NDV42')  # Field name made lowercase.
#     ndv43 = models.FloatField(db_column='NDV43')  # Field name made lowercase.
#     ndv44 = models.FloatField(db_column='NDV44')  # Field name made lowercase.
#     ndv45 = models.FloatField(db_column='NDV45')  # Field name made lowercase.
#     ndv46 = models.FloatField(db_column='NDV46')  # Field name made lowercase.
#     ndv47 = models.FloatField(db_column='NDV47')  # Field name made lowercase.
#     ndv48 = models.FloatField(db_column='NDV48')  # Field name made lowercase.
#     ndv49 = models.FloatField(db_column='NDV49')  # Field name made lowercase.
#     ndv50 = models.FloatField(db_column='NDV50')  # Field name made lowercase.
#     ndv51 = models.FloatField(db_column='NDV51')  # Field name made lowercase.
#     ndv52 = models.FloatField(db_column='NDV52')  # Field name made lowercase.
#     id_crop_plan = models.IntegerField(blank=True, null=True)
#     id_crop_pixel_result = models.IntegerField(blank=True, null=True)
#     id_field = models.ForeignKey(y2019ListOfFields, models.DO_NOTHING, db_column='id_field')
#     comment = models.CharField(blank=True, null=True, max_length=64)

#     class Meta:
#         managed = False
#         db_table = '2019_NDVI_10_1'
#         unique_together = (('x', 'y'))
        

# class y2019Ndvi_20_1(models.Model):
#     geom = models.PointField(blank=True, null=True)
#     x = models.FloatField(db_column='X')  # Field name made lowercase.
#     y = models.FloatField(db_column='Y')  # Field name made lowercase.
#     ndv1 = models.FloatField(db_column='NDV1')  # Field name made lowercase.
#     ndv2 = models.FloatField(db_column='NDV2')  # Field name made lowercase.
#     ndv3 = models.FloatField(db_column='NDV3')  # Field name made lowercase.
#     ndv4 = models.FloatField(db_column='NDV4')  # Field name made lowercase.
#     ndv5 = models.FloatField(db_column='NDV5')  # Field name made lowercase.
#     ndv6 = models.FloatField(db_column='NDV6')  # Field name made lowercase.
#     ndv7 = models.FloatField(db_column='NDV7')  # Field name made lowercase.
#     ndv8 = models.FloatField(db_column='NDV8')  # Field name made lowercase.
#     ndv9 = models.FloatField(db_column='NDV9')  # Field name made lowercase.
#     ndv10 = models.FloatField(db_column='NDV10')  # Field name made lowercase.
#     ndv11 = models.FloatField(db_column='NDV11')  # Field name made lowercase.
#     ndv12 = models.FloatField(db_column='NDV12')  # Field name made lowercase.
#     ndv13 = models.FloatField(db_column='NDV13')  # Field name made lowercase.
#     ndv14 = models.FloatField(db_column='NDV14')  # Field name made lowercase.
#     ndv15 = models.FloatField(db_column='NDV15')  # Field name made lowercase.
#     ndv16 = models.FloatField(db_column='NDV16')  # Field name made lowercase.
#     ndv17 = models.FloatField(db_column='NDV17')  # Field name made lowercase.
#     ndv18 = models.FloatField(db_column='NDV18')  # Field name made lowercase.
#     ndv19 = models.FloatField(db_column='NDV19')  # Field name made lowercase.
#     ndv20 = models.FloatField(db_column='NDV20')  # Field name made lowercase.
#     ndv21 = models.FloatField(db_column='NDV21')  # Field name made lowercase.
#     ndv22 = models.FloatField(db_column='NDV22')  # Field name made lowercase.
#     ndv23 = models.FloatField(db_column='NDV23')  # Field name made lowercase.
#     ndv24 = models.FloatField(db_column='NDV24')  # Field name made lowercase.
#     ndv25 = models.FloatField(db_column='NDV25')  # Field name made lowercase.
#     ndv26 = models.FloatField(db_column='NDV26')  # Field name made lowercase.
#     ndv27 = models.FloatField(db_column='NDV27')  # Field name made lowercase.
#     ndv28 = models.FloatField(db_column='NDV28')  # Field name made lowercase.
#     ndv29 = models.FloatField(db_column='NDV29')  # Field name made lowercase.
#     ndv30 = models.FloatField(db_column='NDV30')  # Field name made lowercase.
#     ndv31 = models.FloatField(db_column='NDV31')  # Field name made lowercase.
#     ndv32 = models.FloatField(db_column='NDV32')  # Field name made lowercase.
#     ndv33 = models.FloatField(db_column='NDV33')  # Field name made lowercase.
#     ndv34 = models.FloatField(db_column='NDV34')  # Field name made lowercase.
#     ndv35 = models.FloatField(db_column='NDV35')  # Field name made lowercase.
#     ndv36 = models.FloatField(db_column='NDV36')  # Field name made lowercase.
#     ndv37 = models.FloatField(db_column='NDV37')  # Field name made lowercase.
#     ndv38 = models.FloatField(db_column='NDV38')  # Field name made lowercase.
#     ndv39 = models.FloatField(db_column='NDV39')  # Field name made lowercase.
#     ndv40 = models.FloatField(db_column='NDV40')  # Field name made lowercase.
#     ndv41 = models.FloatField(db_column='NDV41')  # Field name made lowercase.
#     ndv42 = models.FloatField(db_column='NDV42')  # Field name made lowercase.
#     ndv43 = models.FloatField(db_column='NDV43')  # Field name made lowercase.
#     ndv44 = models.FloatField(db_column='NDV44')  # Field name made lowercase.
#     ndv45 = models.FloatField(db_column='NDV45')  # Field name made lowercase.
#     ndv46 = models.FloatField(db_column='NDV46')  # Field name made lowercase.
#     ndv47 = models.FloatField(db_column='NDV47')  # Field name made lowercase.
#     ndv48 = models.FloatField(db_column='NDV48')  # Field name made lowercase.
#     ndv49 = models.FloatField(db_column='NDV49')  # Field name made lowercase.
#     ndv50 = models.FloatField(db_column='NDV50')  # Field name made lowercase.
#     ndv51 = models.FloatField(db_column='NDV51')  # Field name made lowercase.
#     ndv52 = models.FloatField(db_column='NDV52')  # Field name made lowercase.
#     id_crop_plan = models.IntegerField(blank=True, null=True)
#     id_crop_pixel_result = models.IntegerField(blank=True, null=True)
#     id_field = models.ForeignKey(y2019ListOfFields, models.DO_NOTHING, db_column='id_field')
#     comment = models.CharField(blank=True, null=True, max_length=64)

#     class Meta:
#         managed = False
#         db_table = '2019_NDVI_20_1'
#         unique_together = (('x', 'y'))


# class y2019ListOfAnalysis(models.Model):
#     id_field = models.ForeignKey(y2019ListOfFields, models.DO_NOTHING, db_column='id_field')
#     id_model = models.IntegerField()
#     results = models.CharField(max_length=64)
#     comment = models.CharField(blank=True, null=True, max_length=64)

#     class Meta:
#         managed = False
#         db_table = '2019_list_of_analysis'
#         unique_together = (('id_field', 'id_model'))


# class y2019Mediadate(models.Model):
#     id_field = models.ForeignKey(y2019ListOfFields, models.DO_NOTHING, db_column='id_field')
#     reference = models.CharField(unique=True, max_length=64)
#     geoteg = models.PointField(blank=True, null=True)
#     filming_date = models.DateField(blank=True, null=True)
#     comment = models.CharField(blank=True, null=True, max_length=64)

#     class Meta:
#         managed = False
#         db_table = '2019_mediadate'


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
