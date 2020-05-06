import requests
import time
starttime = time.time()
count = 0
## Ingest in Africa"
Africa_url = 'https://acleddata.com/download/2909/Africa_1997-2020_Apr25.xlsx'
Africa = requests.get(Africa_url, allow_redirects=True)
open("C:\Working\data\\africa.csv", 'wb').write(Africa.content)


count = count +1
endtime = time.time()
totaltime = endtime - starttime
print("Total time to run process: " +str(count) + "--" + str(totaltime))

########################################
## Ingest in Middle East
MiddleEast_url = 'https://acleddata.com/download/2915/'
MiddleEast = requests.get(MiddleEast_url, allow_redirects=True)
open("C:\Working\data\\me.csv", 'wb').write(MiddleEast.content)

count = count +1
endtime = time.time()
totaltime = endtime - starttime
print("Total time to run process: " +str(count) + "--" + str(totaltime))

########################################
#South & Southeast Asia
SSA_url = 'https://acleddata.com/download/18815/'
SSA = requests.get(SSA_url, allow_redirects=True)
open("C:\Working\data\\ssa.csv", 'wb').write(SSA.content)

count = count +1
endtime = time.time()
totaltime = endtime - starttime
print("Total time to run process: " +str(count) + "--" + str(totaltime))

########################################
#Central Asia & the Caucasus
CAC_url = 'https://acleddata.com/download/18750/'
CAC = requests.get(Africa_url, allow_redirects=True)
open("C:\Working\data\\cac.csv", 'wb').write(CAC.content)

count = count +1
endtime = time.time()
totaltime = endtime - starttime
print("Total time to run process: " +str(count) + "--" + str(totaltime))

########################################
#Latin America & the Caribbean
LAC_url = 'https://acleddata.com/download/19657/'
LAC = requests.get(Africa_url, allow_redirects=True)
open("C:\Working\data\\lac.csv", 'wb').write(LAC.content)

count = count +1
endtime = time.time()
totaltime = endtime - starttime
print("Total time to run process: " +str(count) + "--" + str(totaltime))

########################################
#Eastern & Southeastern Europe & the Balkans
SEB_url = 'https://acleddata.com/download/14515/'
SEB = requests.get(SEB_url, allow_redirects=True)
open("C:\Working\data\\seb.csv", 'wb').write(SEB.content)
endtime = time.time()
totaltime = endtime - starttime
print("Total time to run the total process: " + str(totaltime))

https://data.milwaukee.gov/dataset/wibr/resource/87843297-a6fa-46d4-ba5d-cb342fb2d3bb