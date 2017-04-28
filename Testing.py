import zipfile
filename = "90052.txt"
data=[]
z = zipfile.ZipFile("C:\\Users\\jamesw\\Downloads\\channel.zip")

data.append(z.getinfo(filename).comment)

print(data)