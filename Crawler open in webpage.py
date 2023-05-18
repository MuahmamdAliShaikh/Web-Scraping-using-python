import re,os,time
v=[]
def get_files(path,word):
    a=os.scandir(path)
    for i in a:
        if i.is_file():
            x=re.findall(".txt",str(i))
            if x:
                f=open(i,"r")
                d=re.split(r'\s+',f.read())
                if word in d:
                    v.append(i)
                    

            
        else:
            get_files(i.path,word)

def file_info(v=v):
    f=open("crawler.html","w")
    if v==[]:
        print("Not Found")
        message=f'''
           <html>
                <head>
                </head>
                <body>
                <h1>Not Found</h1>
                </body>
            </html>
                 '''
        f.write(message)
        f.close()
    else:
        for i in v:
            print("Name of the File: ",i.name)
            print("Path of the File: ",i.path)
            size=os.path.getsize(i.path)
            print("Size of the File: ",size)
            creat=time.ctime(os.path.getmtime(i.path))
            print("Created date of the File: ",creat)
            mod=time.ctime(os.path.getctime(i.path))
            print("Moderated date of the File: ",mod)
            message=f'''
               <html>
                    <head>
                    </head>
                    <body style="background-color: black">
                    <li type="1" style="color:rgb(232,0,0);font-size:20px">Name of the File: {i.name}</li>
                    <div>
                    <p style="color:lightblue;font-size:20px;text-decoration: underline;font-weight: bold><a href="{i.path}">{i.path}</a></p>
                    <p style="color:rgb(232,0,0);font-size:20px">Size of the File: {size}</p>
                    <p style="color:rgb(232,0,0);font-size:20px">Created date of the File: {creat}</p>
                    <p style="color:rgb(232,0,0);font-size:20px">Moderated date of the File: {mod}</p>
                    </div>
                    </body>
                </html>
                   '''
            f.write(message)
        f.close()
            
get_files("G:\\New folder","Ali")
file_info()


 
