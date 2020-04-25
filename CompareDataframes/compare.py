import pandas as pd
import numpy as np

hazards = pd.read_csv(r'C:\Users\lyle6003\Desktop\comparetables\threats.csv')
threats = pd.read_csv(r'C:\Users\lyle6003\Desktop\comparetables\hazards.csv')
threat_hazards = pd.read_csv(r'C:\Users\lyle6003\Desktop\comparetables\threats_hazards.csv')
impacted_assets = pd.read_csv(r'C:\Users\lyle6003\Desktop\comparetables\impacted_assets.csv')

#def removeClosedEvents(threats,hazards,impacted_assets):
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

# Pull out the two items that are no longer in the combined list.
#t = set(impacted_assets_list) - set(h_t_list)
#tlist=[]

def find_difference(incoming, existing):
    new_dates = list(set(incoming).intersection(set(existing)))
    return new_dates
differance_list = find_difference(impacted_assets_list,h_t_list)
# Filter Datarame with dates that are not in our ArcGIS Online Table
impacted_assets = impacted_assets[impacted_assets['ID'].isin(differance_list)]
print("Differance list")
print(differance_list)
print(h_t_list)
print(impacted_assets_list)
print(impacted_assets)

#Combine the two layers into one
threat_hazard_1 = pd.concat([threats, hazards], ignore_index=True)
#print(threat_hazard_1)

#Example using pandas
unique_h_l = list(threat_hazards['ID'].unique())

#Examples using Numpy
value = np.unique(h_t_list)
print("Unique: ")


print(value)
print(unique_h_l)
print(len(unique_h_l))
print(len(value))
for item in unique_h_l:
    print(item)
    for i in h_t_list:
        if i == item:
            print(i)


