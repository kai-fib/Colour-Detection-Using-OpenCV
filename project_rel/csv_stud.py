import csv
def write():
    f=open("student.csv","w",)
    s_writer=csv.writer(f)
    s_writer.writerow(['RollNo','Name','Marks'])
    rec=[]
    while True:
        r=int(input("enter roll no."))
        n=input("enter name:")
        m=int(input("enter marks::"))
        lst=[r,n,m]
        rec.append(lst)
        ch=input("do yo wanna continue or not (y/n)")
        if ch=='n':
            break
    s_writer.writerows(rec)
    f.close()

def read():
    f=open("student.csv","r")
    s_reader=csv.reader(f)
    for i in s_reader:
        print(i)

write()
read()
