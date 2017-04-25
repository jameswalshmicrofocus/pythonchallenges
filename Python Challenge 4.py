import requests

def geturl():
    loop = 0
    newstr = "8022"
    while loop < 100:

        r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(newstr))
        newstr = r.text
        newstr = newstr.replace("and the next nothing is ", "")
        print(newstr)

geturl()