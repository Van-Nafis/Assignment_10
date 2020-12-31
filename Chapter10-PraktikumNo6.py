
myfile=open("d:/PythonProjects/Teks Asli.txt","r")
teks=myfile.read()
text=list(teks)
print("Masukan n : ",end="")
pergeseran=int(input())


ordnya=[]
for kunci in text:
    x=ord(kunci)
    j=x+pergeseran
    ordnya.append(j)
myfile.close()



fileku=open("d:/PythonProjects/Teks Sandi.txt","w")
for x in ordnya:
    i=str(x)
    
    fileku.write(i)
    fileku.write(" ")
fileku.write("\n")
fileku.write(str(pergeseran))
fileku.close()
        




