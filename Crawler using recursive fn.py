import os,re,time
c=[]
def get_files(path):
    a=os.scandir(path)
    for i in a:
        if i.is_file():
            x=re.findall(".txt",str(i))
            if x:
                f=open(i,"r")
                content=re.findall("[0-9]{1,2}/[0-9]{1,2}/[0-9]{2,4}",f.read())
                if content:
                    c.append(i)
                    
        else:
            get_files(i.path)

    return c

def prop_files(c=c):
    if c==[]:
        print("File not found")
    else:
        for i in range(len(c)):
            path=c[i].path
            name=c[i].name
            mod=time.ctime(os.path.getmtime(c[i].path))
            creat=time.ctime(os.path.getctime(c[i].path))
            size=os.path.getsize(c[i].path)
            print("Name of file is: ",name,"\nPath of file is: ",path,"\nLast modification: ",mod,"\nCreation: ",creat,"\nSize: ",size)    


get_files("G:\\New folder")    
prop_files()



