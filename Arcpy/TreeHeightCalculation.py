# Import modules
import arcpy

# Set Variables
treePts = r"Add your Path here"
buffTrees = r"Add your Path here"
surfaceData = r"Add your Path here"
heightEvaluation = "Z_MAX"
buffDistance = "CanRadius"
print("Variables set.")

# Buffer tree points
arcpy.Buffer_analysis(treePts, buffTrees, buffDistance)
print("Buffer complete")

# Determine tree height
arcpy.AddSurfaceInformation_3d(buffTrees, surfaceData, heightEvaluation)
print("Surface information added")
