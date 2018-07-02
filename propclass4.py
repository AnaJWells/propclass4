import arcpy
import re
import os
from arcpy import env

#Input Parameters
in_fc = arcpy.GetParameterAsText(0)
out_fc = arcpy.GetParameterAsText(1)

#Create copy of feature class in memory
arcpy.FeatureClassToFeatureClass_conversion(in_fc, "in_memory", os.path.basename(out_fc)+"MEMORY")
out_mem = "in_memory\\"+os.path.basename(out_fc)+"MEMORY"

#updateCursor = arcpy.da.UpdateCursor("dunnShort2")
updateCursor = arcpy.UpdateCursor(out_mem)
for row in updateCursor:
    propvalue = row.getValue("PROPCLASS")
    estvalue = row.getValue("ESTFMKVALUE")
    if estvalue is not None and propvalue is not None and (propvalue.find('4') >= 0):
         row.setValue("ESTFMKVALUE", None)
         updateCursor.updateRow(row)  
		 
#Write feature class from memory
arcpy.FeatureClassToFeatureClass_conversion(out_mem, os.path.dirname(out_fc), os.path.basename(out_fc))
arcpy.Delete_management(out_mem)