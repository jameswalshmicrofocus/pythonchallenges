import pickle

pickle_in = open('banner.p', 'rb')
pickle_out = pickle.load(pickle_in)

print((pickle_out))