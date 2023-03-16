# Import the site package
import arcpy

# Define the variables
bufferIn = r"Add your Path here"
bufferOut = r"Add your Path here"

# Perform the analysis
arcpy.analysis.Buffer(bufferIn, bufferOut, "1 Mile")
print("Buffer analysis is complete.")