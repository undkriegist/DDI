import pickle

f = open("test.pkl","rb")
inf = pickle.load(f)
print (inf)
inf=str(inf)
ft = open('test.txt', 'w')  
ft.write(inf) 