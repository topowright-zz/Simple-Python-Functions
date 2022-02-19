import pandas as pd
import time

starttime = time.time()

american_cities = cities.csv



# Combine two feeds into one common feed
for index, row in threats.iterrows():
    threat_hazards = threat_hazards.append(row)

for index, row in hazards.iterrows():
    threat_hazards = threat_hazards.append(row)

# Creating a list
# Copying the threat and hazards into one list
h_t_list = []
for index, row in threat_hazards.iterrows():
    h_t_list.append(row.ID)

impacted_assets_list = []
for index, row in impacted_assets.iterrows():
    impacted_assets_list.append(row.ID)


#---------------------------------
def find_difference(incoming, existing):
    diff_list = list(set(incoming).intersection(set(existing)))
    return diff_list
differance_list = find_difference(impacted_assets_list,h_t_list)
# Filter Datarame with that is not in the combined table
impacted_assets = impacted_assets[impacted_assets['ID'].isin(differance_list)]
#---------------------------------

#Combine the two layers into one
threat_hazard_1 = pd.concat([threats, hazards], ignore_index=True)


#Example using pandas This finds the unique ID's in our list
unique_ids = list(threat_hazards['ID'].unique())

countlist={}
count = 0
for item in unique_ids:
    count = 1
    for i in h_t_list:
        if i == item:
            count = count +1
        countlist[item] = count

print(countlist)
endtime = time.time()



for key, value in countlist.items():
    print(key, value)
    assets.append(key == 'ID')
    assets.append(value == 'count')
print(assets)

# Pull out the two items that are no longer in the combined list.
#t = set(impacted_assets_list) - set(h_t_list)
#tlist=[]
time = endtime - starttime
print(time)