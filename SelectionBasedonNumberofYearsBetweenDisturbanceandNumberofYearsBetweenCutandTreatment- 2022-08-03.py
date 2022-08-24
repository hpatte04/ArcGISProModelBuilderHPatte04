# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2022-08-03 12:05:28
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

        # Process: Add Fields (multiple) (2) (Add Fields (multiple)) (management)
        C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_R2_XX_4_ = arcpy.management.AddFields(in_table=C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_R2_XX, field_description=[["Years2", "DOUBLE", "Years Between 2020 and Cut year", "", "", ""], ["Years1", "LONG", "Between Spray and Cut", "", "", ""]])[0]

        # Process: Calculate Field (Calculate Field) (management)
        C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_R2_XX_2_ = arcpy.management.CalculateField(in_table=C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_R2_XX_4_, field="Years1", expression="2020-!AR_YEAR_13!", expression_type="PYTHON3", code_block="", field_type="TEXT", enforce_domains="NO_ENFORCE_DOMAINS")[0]

        # Process: Calculate Field (4) (Calculate Field) (management)
        C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_XX_R3_3_ = arcpy.management.CalculateField(in_table=C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_R2_XX_2_, field="Year2", expression="!AR_YEAR12!-!AR_YEAR13!", expression_type="PYTHON3", code_block="", field_type="TEXT", enforce_domains="NO_ENFORCE_DOMAINS")[0]

        # Process: Select Layer By Attribute (Select Layer By Attribute) (management)
        with arcpy.EnvManager(scratchWorkspace=r"C:\Users\Heather Patterson\Documents\ArcGIS\Projects\MyProject\MyProject.gdb", workspace=r"C:\Users\Heather Patterson\Documents\ArcGIS\Projects\MyProject\MyProject.gdb"):
            C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_R2_XX_3_, Count = arcpy.management.SelectLayerByAttribute(in_layer_or_view=C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_XX_R3_3_, selection_type="NEW_SELECTION", where_clause="Years2 >= 10 And Years1 >= 3 And Years1 <= 5", invert_where_clause="")

        # Process: Add Fields (multiple) (Add Fields (multiple)) (management)
        C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_XX_R3_7_ = arcpy.management.AddFields(in_table=C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_XX_R3, field_description=[["Years2", "DOUBLE", "Years Between 2020 and Cut year", "", "", ""], ["Years1", "LONG", "Between Spray and Cut", "", "", ""]])[0]

        # Process: Calculate Field (2) (Calculate Field) (management)
        C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_XX_R3_6_ = arcpy.management.CalculateField(in_table=C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_XX_R3_7_, field="Year2", expression="2020-!AR_YEAR_13!", expression_type="PYTHON3", code_block="", field_type="TEXT", enforce_domains="NO_ENFORCE_DOMAINS")[0]

        # Process: Calculate Field (3) (Calculate Field) (management)
        C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_XX_R3_5_ = arcpy.management.CalculateField(in_table=C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_XX_R3_6_, field="Year2", expression="!AR_YEAR12!-!AR_YEAR13!", expression_type="PYTHON3", code_block="", field_type="TEXT", enforce_domains="NO_ENFORCE_DOMAINS")[0]

        # Process: Select Layer By Attribute (2) (Select Layer By Attribute) (management)
        with arcpy.EnvManager(scratchWorkspace=r"C:\Users\Heather Patterson\Documents\ArcGIS\Projects\MyProject\MyProject.gdb", workspace=r"C:\Users\Heather Patterson\Documents\ArcGIS\Projects\MyProject\MyProject.gdb"):
            C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_XX_R3_2_, Count_2_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=C1_F1_XX_XX_XX_XX_XX_T1_XX_XX_XX_XX_R3_5_, selection_type="NEW_SELECTION", where_clause="Years2 >= 10 And Years1 >= 3 And Years1 <= 5", invert_where_clause="NON_INVERT")

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