myfile=open("d:/PythonProjects/rangkaianbilangan.txt","r")

teks=myfile.readlines()
i=0

for j in teks:
    z=[]
    text=teks[i].split("|")
    data=text[1].split("\n")
    z.append(int(text[0]))
    z.append(int(data[0]))
    print(sum(z))
    i=i+1
    
