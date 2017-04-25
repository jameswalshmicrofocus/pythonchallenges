from os import listdir
from os.path import isfile, join
mypath = 'C:\\Users\\James\\Downloads\\channel\\'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
count = 0
for file in onlyfiles:
    filename = file
    path = mypath + filename
    with open(path, 'r') as myfile:
        data = myfile.read().replace('\n', '')
        print(data)
        data = data.replace("Next nothing is ", "")
        filename = data
        filename = filename + ".txt"
        count = count + 1

print(count)