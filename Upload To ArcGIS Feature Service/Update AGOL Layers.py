from arcgis.gis import GIS
import pandas as pd
import os

# Inputs for script:
# Input the name of the file that we will be pushing to AGOL
filename= 'filename'
gis_id = 'item id'

#Username and Password for AGOL
username = "Emter your username"
password = "Emter your password"
org_url = r"Enter your ArcGIS online URL"
gis = GIS(org_url, username, password)
print("Successfully logged in as: " + gis.properties.user.username)


##############################################################################################

#Create a dataframe from a layer
item = gis.content.get(gis_id)
item_lyr = item.layers[0]
gis_df = item_lyr.query(return_geometry=True).sdf


#Functions used to update and pull data
def batch_it(l, n):

    for i in range(0, len(l), n):
        yield l[i:i + n]

def createCSVPath(filename):
    path = os.path.abspath('')
    csv_path = path + "/" + filename
    return csv_path

mycsv = createCSVPath(filename)

#Remove the data from the layer in AGOL; We will add the data in the next step
item_lyr.manager.truncate()

# Read the csv file from local directory into a pandas dataframe:
df = pd.read_csv(mycsv)
print("The csv that is being read into AGOL is: " + mycsv)
print(gis_df)


#Push the content into the gis layer identified above
update_sets = list(batch_it(df.spatial.to_featureset().features, 1000))
for edits in update_sets:
    res = item_lyr.edit_features(adds=edits, rollback_on_failure=False)['addResults']
    print(f"Added {len([i for i in res if i['success']])} rows of {len(edits)}")
