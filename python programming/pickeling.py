#pickeling
import pickle

fruits=['mango','banana','apple','123','xxxx']

file_pickle=open('fruits.data','wb')
pickle.dump(fruits,file_pickle)
file_pickle.close()

print(fruits)
del fruits


import_pickle_data=open('fruits.data','rb')
f_pickle=pickle.load(import_pickle_data)
import_pickle_data.close()

print(f_pickle)
