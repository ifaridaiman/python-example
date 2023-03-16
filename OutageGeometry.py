import arcpy,csv



arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(103501)

outageXY =r"Add your Path here"
outConvexHull = r"Add your Path here"
outputJoin = r"in_memory\outputJoin"
serviceAreas = r"Add your Path here"

outageCoords = []


csvFile = open(outageXY)
csvReader = csv.reader(csvFile)

next(csvReader)

# Append coordinates from csv in a list

for row in csvReader:
    outageCoords.append(row)


# Create multipoint geometry from list of coordinates
outagePoints = (arcpy.Multipoint(arcpy.Array([arcpy.Point(*coords) for coords in outageCoords])))
print("Geometry object created.")


# Create outage boundary using convex hull
convexHull = outagePoints.convexHull()
arcpy.CopyFeatures_management(convexHull, outConvexHull)

arcpy.SpatialJoin_analysis(serviceAreas,outagePoints, outputJoin)

sField = ['Join_Count','ServArNu']

exp = '"Join_Count"=1'

with arcpy.da.SearchCursor(outputJoin,sField) as sCursor:
    for row in sCursor:
        print("Affected service areas")
        print("Service Area: {}".format(row[1]))

