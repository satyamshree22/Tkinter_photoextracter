from tkinter import *
import os,glob,shutil,time
from PIL import ImageTk,Image
import time



root =Tk()
root.title("Photo Manager")
scrip="FILES FOUND\n"

                 

def extract(scrip):
    count = 0
    content =os.listdir()
    if 'photos' not in content:
        os.mkdir('photos')
    source_to=os.path.abspath('photos')
    source_from=os.path.abspath(display.get())
    print(source_from)
    for items in glob.glob(source_from+'/*.jpg'):
        content_to=os.listdir(source_to)
        item=os.path.basename(items)
        if item not in content_to:
            shutil.copy(items,source_to)
            scrip=scrip+item+"\n"
            count=count+1
            time.sleep(.7)
        


    for items in glob.glob(source_from+'/*.jpeg'):
        content_to=os.listdir(source_to)
        item=os.path.basename(items)
        if item not in content_to:
            shutil.copy(items,source_to)
            scrip=scrip+item+"\n"
            count=count+1
            time.sleep(.7)
            


    
    for items in glob.glob(source_from+'/*.png'):
        content_to=os.listdir(source_to)
        item=os.path.basename(items)
        if item not in content_to:
            shutil.copy(items,source_to)
            scrip=scrip+item+"\n"
            count=count+1
            time.sleep(.7)


             
    count=str(count)
    scrip=scrip+"files found="+count+"\n"
    T.insert(END,scrip)
    display.delete(0,END)
    display.insert(0,"task done")

display = Entry(root,width=75)
display.grid(row=0,column=0,columnspan=3)
T=Text(root, height=5, width=60)

T.insert(END,scrip)




T.grid(row=1,column=0,columnspan=2)
botton_start=Button(root,text="extract",padx=25,pady=30,background='SteelBlue4',command=lambda:extract(scrip))



botton_start.grid(row=1,column=3,columnspan=1)









root.mainloop()



