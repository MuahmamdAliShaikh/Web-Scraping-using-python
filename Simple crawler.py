import os,re,time

##def get_file(path):
##    a = os.scandir(path)
##    for i in a:
##        if i.is_file():
##            #st=i.stat()
##            x=re.findall(".txt",str(i))
##            if x:
##                f=open(i,"r")
##                content=re.findall("[0-9]{1,2}/[0-9]{1,2}/[0-9]{2,4}",f.read())
##                
##                if content:
##                    print("The path of file is: ",i.path,"\nThe name of file is: ",i.name)
##                    print("Last modification: ",time.ctime(os.path.getmtime(i.path)))#time.ctime is used to convert in local time 
##                    print("Creation: ",time.ctime(os.path.getctime(i.path)))
##                    print("Size: ",os.path.getsize(i.path))
##                    print(content)
##                    #print("\nThe time of most recent access: ",st[7],"\nThe time of most recent modification: ",st[8],"\nThe size of the file: ",st[6])
##        else:
##            get_file(i.path)
##            
##        
##get_file("G:\\New folder")
##c=re.findall("Ali","jmn;lkan;c:lnajnka;ali jdnsao ALi",flags=re.IGNORECASE)
##print(c)

##d=re.findall("[0-9]{1,2}/[0-9]{1,2}/[0-9]{2,4}","akdnvcxk 01/23/2005 jkljs 1/2/05goijndsdl")
##print(d)

user_email="alisheikhmrss1260ue@gmail.com"
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
if re.search(email_condition,user_email):
    print("Correct email_condition")
else:
    print("InCorect email_condition")


##a=os.scandir("G:\\New folder")
##for i in a:
##    if i.is_file():
##        x=re.findall(".txt",str(i))
##        print(x)

    
