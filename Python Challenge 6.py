import zipfile
i = 100
list=[]
filename = "90052.txt"
z = zipfile.ZipFile("C:\\Users\\jamesw\\Downloads\\channel.zip")
while i > 8:

    path = "C:\\Users\\jamesw\\Downloads\\channel\\"+filename
    try:
        with open(path, 'r') as myfile:
            data = myfile.read().replace('\n', '')
            # print(data)
            data = data.replace("Next nothing is ", "")
            filename = data
            filename = filename+".txt"
            list.append(z.getinfo(filename).comment)
    except:
        break


for list in list:
    print(list)

