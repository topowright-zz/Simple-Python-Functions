import os
# Please enter the file
filename = 'SampleUpload.csv'


def createCSVPath(filename):
    path = os.path.dirname(__file__)
    mycsv = "r" + path + "\\" + filename
    return mycsv

csv = createCSVPath(filename)
print(csv)