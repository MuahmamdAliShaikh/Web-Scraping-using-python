import re,os,time
class Crawler:
    def __init__(s,word):
        s.word=word
        s.list=[]
    def get_files(s,path):
        a=os.scandir(path)
        for i in a:
            if i.is_file():
                x=re.findall(".txt",str(i))
                if x:
                    f=open(i,"r")
                    d=re.split(r'\s+',f.read())
                    if s.word in d:
                        s.list.append(i)
            else:
                s.get_files(i.path)
        return s.list
    def file_empty(s):
        if s.list==[]:
            print("File not found")
    def file_name(s):
        for i in s.list:
            print("Name of File: ",i.name)
    def file_path(s):
        for i in s.list:
            print("Path of File: ",i.path)
    def file_size(s):
        for i in s.list:
            print("Size of File: ",i.stat()[6])
    def file_mod(s):
        for i in s.list:
            mod=time.ctime(os.path.getmtime(i.path))
            print("Modified date of File: ",mod)
    def file_create(s):
        for i in s.list:
            creat=time.ctime(os.path.getctime(i.path))
            print("Created date of File: ",creat)

    def open_webpage(s):
        f=open("web.html","w")
        if s.list==[]:
            message=f'''
               <html>
                    <head>
                    </head>
                    <body>
                    <h1>fILE NOT FOUND</h1>
                    </body>
                </html>
                     '''
            f.write(message)
            f.close()
        else:
            for i in s.list:
                message=f'''
                       <html>
                            <head>
                            </head>
                            <body style="background-color: pink">
                            <li>Name of the File: {i.name}</li>
                            <div>
                            <p><a href="{i.path}">{i.path}</a></p>
                            <p>Size of the File: {i.stat()[6]}</p>
                            <p>Created date of the File: {time.ctime(os.path.getmtime(i.path))}</p>
                            <p>Moderated date of the File: {time.ctime(os.path.getmtime(i.path))}</p>
                            </div>
                            </body>
                        </html>
                           '''
                f.write(message)
            f.close()

    
                
a=Crawler(input("Enter the Searching word: "))
a.get_files(input("Enter the Directory: "))
a.file_name()
a.file_path()
a.file_size()
a.file_empty()
a.file_mod()
a.file_create()
a.open_webpage()

