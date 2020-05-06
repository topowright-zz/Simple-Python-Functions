import requests
import time
url = 'https://data.milwaukee.gov/dataset/e5feaad3-ee73-418c-b65d-ef810c199390/resource/87843297-a6fa-46d4-ba5d-cb342fb2d3bb/download/wibr.csv'
myfile = requests.get(url, allow_redirects=True)
open("C:\Working\data\\file.csv", 'wb').write(myfile.content)



