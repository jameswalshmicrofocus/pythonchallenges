import pickle

pickle_in = open("banner.p", "rb")
output = pickle.load(pickle_in)
print(output)