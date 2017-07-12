import re
with open('enable1.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
for match in re.findall('[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}',data, re.DOTALL):
    print (match)
    
    print("Hello There")
