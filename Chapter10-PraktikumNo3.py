myfile=open("d:/PythonProjects/nimlnamalalamat.txt","r")

teks=myfile.readlines()
dataMhs=[]
i=0

for j in teks:
    text=teks[i].split("|")
    data=text[2].split("\n")
    alamat=data[0]
    dataakhir={}
    dataakhir["nim"]=text[0]
    dataakhir["nama"]=text[1]
    dataakhir["alamat"]=alamat
    dataMhs.append(dataakhir)
    i=i+1



myfile.close
print(dataMhs)
