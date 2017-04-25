import pickle

pickle_in = open("banner.p", "rb")
output = pickle.load(pickle_in)
print(output)

for line in output:
    print(''.join(c * n for c, n in line))