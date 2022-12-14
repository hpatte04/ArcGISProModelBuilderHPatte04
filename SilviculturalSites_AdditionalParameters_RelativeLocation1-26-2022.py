# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2022-01-26 12:06:43
"""
import arcpy
import os

def FeatureClassGenerator(workspace, wild_card, feature_type, recursive) :
  with arcpy.EnvManager(workspace = workspace):

    dataset_list = [""]
    if recursive:
      datasets = arcpy.ListDatasets()
      dataset_list.extend(datasets)

    for dataset in dataset_list:
      featureclasses = arcpy.ListFeatureClasses(wild_card, feature_type, dataset)
      for fc in featureclasses:
        yield os.path.join(workspace, dataset, fc), fc


def SilviculturalSites_AdditionalParameters_RelativeLocation():  # SilviculturalSites_AdditionalParameters_RelativeLocation

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Model Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb", workspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb"):
        FinalSilviculturalSiteHistorySPLIT_gdb = "F:\\ModelFiles\\SilviculturalSites\\IntermediateSilvicultureFiles\\SiteHistory\\FinalSilviculturalSiteHistorySPLIT.gdb"
        Tend_Prot_2_ = "C:\\Users\\heath\\Downloads\\AR_Master.gdb\\AR_Master.gdb\\Tend\\Tend_Prot"
        Fire_Disturbance_Area = "Fire_Disturbance_Area"
        False_72 = False
        FinalSilviculturalSiteHistoryGDB_gdb = "F:\\ModelFiles\\SilviculturalSites\\IntermediateSilvicultureFiles\\SiteHistory\\FinalSilviculturalSiteHistoryGDB.gdb"
        FinalSilviculturalSiteHistoryGDB_gdb_2_ = "F:\\ModelFiles\\SilviculturalSites\\IntermediateSilvicultureFiles\\SiteHistory\\FinalSilviculturalSiteHistoryGDB.gdb"

        for C, Name in FeatureClassGenerator(FinalSilviculturalSiteHistorySPLIT_gdb, "", "", "NOT_RECURSIVE"):

            # Process: Copy Features (4) (Copy Features) (management)
            Tend_Prot = "F:\\ModelFiles\\OriginalFiles\\OriginalFiles.gdb\\Tend_Prot"
            with arcpy.EnvManager(scratchWorkspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb", workspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb"):
                arcpy.management.CopyFeatures(in_features=Tend_Prot_2_, out_feature_class=Tend_Prot, config_keyword="", spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None)

            # Process: Select Layer By Location (3) (Select Layer By Location) (management)
            with arcpy.EnvManager(scratchWorkspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb", workspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb"):
                C1_F1_P1_P2_XX_XX_XX_T1_XX_X, Output_Layer_Names_3_, Count_2_ = arcpy.management.SelectLayerByLocation(in_layer=[C, C], overlap_type="WITHIN_A_DISTANCE", select_features=Tend_Prot, search_distance="60 Meters", selection_type="NEW_SELECTION", invert_spatial_relationship="INVERT")

            # Process: Copy Features (2) (Copy Features) (management)
            Name = "C"
            _Name_MOD1 = fr"F:\ModelFiles\SilviculturalSites\IntermediateSilvicultureFiles\AdditionalSelectionParameters\RelativeLocation\IntermediateSilviculturalRelativeLocationFiles.gdb\{Name}MOD1"
            with arcpy.EnvManager(scratchWorkspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb", workspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb"):
                arcpy.management.CopyFeatures(in_features=C1_F1_P1_P2_XX_XX_XX_T1_XX_X, out_feature_class=_Name_MOD1, config_keyword="", spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None)

            # Process: Copy Features (5) (Copy Features) (management)
            Fire_DisturbanceLIO = "F:\\ModelFiles\\OriginalFiles\\OriginalFiles.gdb\\Fire_DisturbanceLIO"
            with arcpy.EnvManager(scratchWorkspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb", workspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb"):
                arcpy.management.CopyFeatures(in_features=Fire_Disturbance_Area, out_feature_class=Fire_DisturbanceLIO, config_keyword="", spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None)

            # Process: Select Layer By Location (2) (Select Layer By Location) (management)
            with arcpy.EnvManager(scratchWorkspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb", workspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb"):
                _Name_60mFire_2_, Output_Layer_Names_2_, Count_3_ = arcpy.management.SelectLayerByLocation(in_layer=[_Name_MOD1], overlap_type="WITHIN_A_DISTANCE", select_features=Fire_DisturbanceLIO, search_distance="60 Meters", selection_type="NEW_SELECTION", invert_spatial_relationship="INVERT")

            # Process: Copy Features (3) (Copy Features) (management)
            _Name_MOD2 = fr"F:\ModelFiles\SilviculturalSites\IntermediateSilvicultureFiles\AdditionalSelectionParameters\RelativeLocation\IntermediateSilviculturalRelativeLocationFiles.gdb\{Name}MOD2"
            with arcpy.EnvManager(scratchWorkspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb", workspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb"):
                arcpy.management.CopyFeatures(in_features=_Name_60mFire_2_, out_feature_class=_Name_MOD2, config_keyword="", spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None)

            # Process: Copy Features (Copy Features) (management)
            _Name_ = fr"F:\ModelFiles\SilviculturalSites\IntermediateSilvicultureFiles\AdditionalSelectionParameters\RelativeLocation\FinalSilviculturalRelativeLocationFiles.gdb\{Name}"
            with arcpy.EnvManager(scratchWorkspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb", workspace=r"C:\Users\heath\Downloads\Masters Data- Chapter 2\Masters Data- Chapter 2\Default.gdb"):
                arcpy.management.CopyFeatures(in_features=_Name_MOD2, out_feature_class=_Name_, config_keyword="", spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None)

if __name__ == '__main__':
    SilviculturalSites_AdditionalParameters_RelativeLocation()
