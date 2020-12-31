myfile=open("d:/PythonProjects/Teks Sandi.txt","r")
teks=myfile.read()
text=teks.split(" ")
akhir=teks.split("\n")
akhiri=int(akhir[1])
texti=" ".join(akhir)
listtexti=texti.split(" ")
data=[]
for huruf in listtexti:
    abjad=int(huruf)
    abjad=abjad-akhiri
    x=chr(abjad)
    print(x)
    data.append(x)

print(data)
myfile.close()

fileku=open("d:/PythonProjects/Teks Asli 2.txt","w")
for i in data:
    fileku.write(i)

fileku.close()
