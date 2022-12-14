# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2022-07-26 16:55:55
"""
import arcpy

def SelectionBasedonNumberofYearsBetweenDisturbanceandNumberofYearsBetweenCutandTreatment():  # SelectionBasedonNumberofYearsBetweenDisturbanceandNumberofYearsBetweenCutandTreatment

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Model Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\Heather Patterson\Documents\ArcGIS\Projects\MyProject\MyProject.gdb", workspace=r"C:\Users\Heather Patterson\Documents\ArcGIS\Projects\MyProject\MyProject.gdb"):
        C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_R2_XX = "T1- Chemical Tending (Aerial)\\C1-F1-XX-XX-XX-XX-XX-T1-XX-XX-XX-R2-XX"
        C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_XX_R3 = "T1- Chemical Tending (Aerial)\\C1-F1-XX-XX-XX-XX-XX-T1-XX-XX-XX-XX-R3"
        C1_F1_XX_XX_XX_XX_XX_XX_XX_XX_XX_XX_R3 = "0- No Treat\\C1-F1-XX-XX-XX-XX-XX-XX-XX-XX-XX-XX-R3"
        C1_F1_XX_XX_XX_XX_XX_XX_XX_XX_XX_R2_XX = "0- No Treat\\C1-F1-XX-XX-XX-XX-XX-XX-XX-XX-XX-R2-XX"

        # Process: Select Layer By Attribute (Select Layer By Attribute) (management)
        with arcpy.EnvManager(scratchWorkspace=r"C:\Users\Heather Patterson\Documents\ArcGIS\Projects\MyProject\MyProject.gdb", workspace=r"C:\Users\Heather Patterson\Documents\ArcGIS\Projects\MyProject\MyProject.gdb"):
            C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_R2_XX_3_, Count = arcpy.management.SelectLayerByAttribute(in_layer_or_view=C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_R2_XX, selection_type="NEW_SELECTION", where_clause="Years2 >= 10 And Years1 >= 3 And Years1 <= 5", invert_where_clause="")

        # Process: Select Layer By Attribute (2) (Select Layer By Attribute) (management)
        with arcpy.EnvManager(scratchWorkspace=r"C:\Users\Heather Patterson\Documents\ArcGIS\Projects\MyProject\MyProject.gdb", workspace=r"C:\Users\Heather Patterson\Documents\ArcGIS\Projects\MyProject\MyProject.gdb"):
            C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_XX_R3_2_, Count_2_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_XX_R3, selection_type="NEW_SELECTION", where_clause="Years2 >= 10 And Years1 >= 3 And Years1 <= 5", invert_where_clause="NON_INVERT")

        # Process: Copy Features (Copy Features) (management)
        C1F1XXXXXXXXXXT1XXXXXXR2XX_3to510to12_shp = "C:\\Users\\Heather Patterson\\Documents\\ArcGIS\\Projects\\MyProject\\SHP-1-26-2022\\C1F1XXXXXXXXXXT1XXXXXXR2XX_3to510to12.shp"
        with arcpy.EnvManager(scratchWorkspace=r"C:\Users\Heather Patterson\Documents\ArcGIS\Projects\MyProject\MyProject.gdb", workspace=r"C:\Users\Heather Patterson\Documents\ArcGIS\Projects\MyProject\MyProject.gdb"):
            arcpy.management.CopyFeatures(in_features=C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_R2_XX_3_, out_feature_class=C1F1XXXXXXXXXXT1XXXXXXR2XX_3to510to12_shp, config_keyword="", spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None)

        # Process: Copy Features (2) (Copy Features) (management)
        C1F1XXXXXXXXXXT1XXXXXXXXR3_3to510to12_shp = "C:\\Users\\Heather Patterson\\Documents\\ArcGIS\\Projects\\MyProject\\SHP-1-26-2022\\C1F1XXXXXXXXXXT1XXXXXXXXR3_3to510to12.shp"
        with arcpy.EnvManager(scratchWorkspace=r"C:\Users\Heather Patterson\Documents\ArcGIS\Projects\MyProject\MyProject.gdb", workspace=r"C:\Users\Heather Patterson\Documents\ArcGIS\Projects\MyProject\MyProject.gdb"):
            arcpy.management.CopyFeatures(in_features=C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_XX_R3_2_, out_feature_class=C1F1XXXXXXXXXXT1XXXXXXXXR3_3to510to12_shp, config_keyword="", spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None)

        # Process: Select Layer By Attribute (4) (Select Layer By Attribute) (management)
        C1_F1_XX_XX_XX_XX_XX_XX_XX_XX_XX_XX_R3_2_, Count_4_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=C1_F1_XX_XX_XX_XX_XX_XX_XX_XX_XX_XX_R3, selection_type="NEW_SELECTION", where_clause="AR_YEAR_13 <= 2010 And AR_YEAR_13 >= 2008", invert_where_clause="")

        # Process: Select Layer By Attribute (3) (Select Layer By Attribute) (management)
        C1_F1_XX_XX_XX_XX_XX_XX_XX_XX_XX_R2_XX_2_, Count_3_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=C1_F1_XX_XX_XX_XX_XX_XX_XX_XX_XX_R2_XX, selection_type="NEW_SELECTION", where_clause="AR_YEAR_13 <= 2010 And AR_YEAR_13 >= 2008", invert_where_clause="")

        # Process: Copy Features (3) (Copy Features) (management)
        C1F1XXXXXXXXXXXXXXXXXXR2XX_10to12_shp = "C:\\Users\\Heather Patterson\\Documents\\ArcGIS\\Projects\\MyProject\\SHP-1-26-2022\\C1F1XXXXXXXXXXXXXXXXXXR2XX_10to12.shp"
        arcpy.management.CopyFeatures(in_features=C1_F1_XX_XX_XX_XX_XX_XX_XX_XX_XX_R2_XX_2_, out_feature_class=C1F1XXXXXXXXXXXXXXXXXXR2XX_10to12_shp, config_keyword="", spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None)

        # Process: Copy Features (4) (Copy Features) (management)
        C1F1XXXXXXXXXXXXXXXXXXXXR3_10to12_shp = "C:\\Users\\Heather Patterson\\Documents\\ArcGIS\\Projects\\MyProject\\SHP-1-26-2022\\C1F1XXXXXXXXXXXXXXXXXXXXR3_10to12.shp"
        arcpy.management.CopyFeatures(in_features=C1_F1_XX_XX_XX_XX_XX_XX_XX_XX_XX_XX_R3_2_, out_feature_class=C1F1XXXXXXXXXXXXXXXXXXXXR3_10to12_shp, config_keyword="", spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None)

if __name__ == '__main__':
    SelectionBasedonNumberofYearsBetweenDisturbanceandNumberofYearsBetweenCutandTreatment()
