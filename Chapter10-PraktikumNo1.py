myfile=open("D:\hello.txt","r")

data=myfile.readlines()
for i in range(0,len(data)):
    data[i]=int(data[i])

bilgenap=0
bilganjil=0
i=0

for j in data:
    if j%2==0:
        bilgenap=bilgenap+1
    elif j%2!=0:
        bilganjil=bilganjil+1

print("Banyaknya Bilangan Genap : ",bilgenap)
print("Banyaknya Bilangan Ganjil : ",bilganjil)
myfile.close()

