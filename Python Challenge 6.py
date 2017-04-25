i = 100
filename = "90052.txt"
while i > 8:

    path = "C:\\Users\\James\\Downloads\\channel\\"+filename
    with open(path, 'r') as myfile:
        data = myfile.read().replace('\n', '')
        print(data)
        data = data.replace("Next nothing is ", "")
        filename = data
        filename = filename+".txt"
