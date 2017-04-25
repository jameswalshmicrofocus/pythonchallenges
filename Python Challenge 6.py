filename = "90052.txt"
path = "C:\\Users\\James\\Downloads\\channel\\"+filename

with open(path, 'r') as myfile:
    data = myfile.read().replace('\n', '')
    print(data)
