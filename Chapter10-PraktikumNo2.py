myfile=open("d:/PythonProjects/nimlnamalalamat.txt","a")
while True:
    print("Masukan NIM\t : ",end="")
    nim=myfile.write(input())
    myfile.write("|")
    print("Masukan Nama Mhs : ",end="")
    nama=myfile.write(input())
    myfile.write("|")
    print("Masukan Alamat\t : ",end="")
    alamat=myfile.write(input())
    myfile.write("\n")
    print("Ulangi input lagi(y/n)\t : ",end="")
    lagi=input()
    if lagi=="n":
        break
myfile.close()
