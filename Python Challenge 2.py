string = "http//www.pythonchallenge.com/pc/def/map.html"
alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz , ,.'.'()()/ / / /"
#Comment to test connect decrypted_message =a new test comment
to_list = ([str(i) for i in str(string)])
to_alphabet = ([str(i) for i in str(alphabet)])

for characters in string:
        firstvar = to_alphabet.index(characters)
        firstvar = firstvar + 2
        decrypted_message.append(alphabet[firstvar])


makeitastring = ''.join(map(str, decrypted_message))
print(makeitastring)

#comment 2
