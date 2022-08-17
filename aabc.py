from doctest import master
from tkinter import *
import tkinter
import tkinter as tk
from tkinter import Message, Text
from turtle import delay
import cv2
import os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import csv
import time
import tkinter.ttk as ttk
import tkinter.font as font
from pathlib import Path
from datetime import datetime
from tkinter.ttk import *
import numpy as np
from pkg_resources import UnknownExtra


class App:
    
    def project():
        
        master = tk.Tk()
        master.geometry('900x700')
        Label(master,text="Advance Security & Attendance System").pack()
        f1=LabelFrame(master)
        f1.pack()
        l1=Label(f1)
        l1.pack()
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("TrainingLabelImage/Trainner.yml")
        harcascadePath = "code/hdd/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)
        df = pd.read_csv("student_details/student_data.csv")
        # url='http://192.168.43.1:8080/video'
        width= 500
        height =500
        
        cam = cv2.VideoCapture(0)
       
        font = cv2.FONT_HERSHEY_SIMPLEX	

        def gate_cam_data():
            root = Tk()
            root.title("Entry record of gate")
            width = 500
            height = 400
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            root.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root.resizable(0, 0)


            TableMargin = Frame(root, width=500)
            TableMargin.pack(side=TOP)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
            tree = ttk.Treeview(TableMargin, columns=("Name", "Time","Date"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            
            tree.heading('Name', text="Name", anchor=W)
            tree.heading('Time', text="Time", anchor=W)
            tree.heading('Date', text="Date", anchor=W)
            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=50)
            tree.column('#2', stretch=NO, minwidth=0, width=150)
            # tree.column('#3', stretch=NO, minwidth=0, width=180)
            tree.pack()

            with open('E:\col_project\entry_record.csv') as f:
                reader = csv.DictReader(f, delimiter=',')
                a=0
                for row in reader:
                    
                   
                    Name = row['Name']
                    Time= row['Time']
                    Date = row['Date']
                    tree.insert("", a, values=(Name,Time,Date))
                    a +=1
        def unknownimages():
            pass

        def openNewWindow():

            window = tk.Tk()
            window.title("Hii Welocome to project")
            window.configure(background ='white')
            window.geometry("625x650")

            def student():
                window = tk.Tk()
                window.title("Student Entry Block")
                window.configure(background ='white')
                window.geometry("625x650")

                message = tk.Label(window, text ="Student Entry",bg ="green", fg = "white", width = 38,height = 3, font = ('times', 20, 'bold'))
                message.place(x =5, y = 5)
                
                lbl = tk.Label(window, text = "Enter Student Id :- ",
                width = 20, height = 2, fg ="green",
                bg = "white", font = ('times', 15, ' bold ') )
                lbl.place(x = 5, y = 190)

                txt = tk.Entry(window,
                width = 20, bg ="white",
                fg ="green", font = ('times', 15, ' bold '))
                txt.place(x = 230, y = 200)

                lbl2 = tk.Label(window, text ="Enter Student Name :-",
                width = 20, fg ="green", bg ="white",
                height = 2, font =('times', 15, ' bold '))
                lbl2.place(x = 5, y = 320)

                txt2 = tk.Entry(window, width = 20,
                bg ="white", fg ="green",
                font = ('times', 15, ' bold ') )
                txt2.place(x = 230, y = 330)
                
                def is_number(s):
                    try:
                        float(s)
                        return True
                    except ValueError:
                        pass

                    try:
                        import unicodedata
                        unicodedata.numeric(s)
                        return True
                    except (TypeError, ValueError):
                        pass

                    return False
                def TakeImages():	
                    
                    
                    Id =(txt.get())
                    name =(txt2.get())
                    
                
                    if(is_number(Id) and name.isalpha()):
                        
                        cam = cv2.VideoCapture(0)
                    
                        harcascadePath = "code/hdd/haarcascade_frontalface_default.xml"
                    
                        detector = cv2.CascadeClassifier(harcascadePath)
                    
                        sampleNum = 0
                        while(True):
                        
                            ret, img = cam.read()
                            
                            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                            
                            faces = detector.detectMultiScale(gray, 1.3, 5)
                            
                        
                            for (x, y, w, h) in faces:
                            
                                cv2.rectangle(img, (x, y), (
                                    x + w, y + h), (255, 0, 0), 2)
                                sampleNum = sampleNum + 1
                                
                                cv2.imwrite(
                                    "data_img/ "+name +"."+Id +'.'+ str(
                                        sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                            
                                cv2.imshow('frame', img)
                        
                            if cv2.waitKey(100) & 0xFF == ord('q'):
                                break
                            
                            elif sampleNum>60:
                                break
                    
                        cam.release()
                    
                        cv2.destroyAllWindows()
                    
                        res = "Images Saved for ID : " + Id +" Name : "+ name
                        
                        row = [Id, name]
                        with open('student_details/student_data.csv', 'a+') as csvFile:
                            writer = csv.writer(csvFile)
                        
                            writer.writerow(row)
                        csvFile.close()
                        message.configure(text = res)
                    else:
                        if(is_number(Id)):
                            res = "Enter Alphabetical Name"
                            message.configure(text = res)
                        if(name.isalpha()):
                            res = "Enter Numeric Id"
                            message.configure(text = res)
                    
                    
                def TrainImages():
                
                    recognizer = cv2.face.LBPHFaceRecognizer_create()
                    
                    harcascadePath = "code/hdd/haarcascade_frontalface_default.xml"
            
                    detector = cv2.CascadeClassifier(harcascadePath)
                
                    faces, Id = getImagesAndLabels("data_img")
                
                    recognizer.train(faces, np.array(Id))	
                    recognizer.save("TrainingLabelImage\Trainner.yml")
                
                    res = "Image Trained"
                    message.configure(text = res)

                def getImagesAndLabels(path):
                
                    imagePaths =[os.path.join(path, f) for f in os.listdir(path)]
                    faces =[]
                
                    Ids =[]
                
                    for imagePath in imagePaths:

                        pilImage = Image.open(imagePath).convert('L')
                        imageNp = np.array(pilImage, 'uint8')
                        Id = int(os.path.split(imagePath)[-1].split(".")[1])
                        faces.append(imageNp)
                        Ids.append(Id)	
                    return faces, Ids

                
                takeImg = tk.Button(window, text ="Take Images",command = TakeImages, fg ="white", bg ="green",
                width = 15, height = 3, activebackground = "Red",
                font =('times', 15, ' bold '))
                takeImg.place(x = 10, y = 500)

                trainImg = tk.Button(window, text ="Train Model",
                command = TrainImages, fg ="white", bg ="green",
                width = 15, height = 3, activebackground = "Red",
                font =('times', 15, ' bold '))
                trainImg.place(x = 215, y = 500)

            
                quitWindow = tk.Button(window, text ="Quit",
                command = window.destroy, fg ="white", bg ="green",
                width = 15, height = 3, activebackground = "Red",
                font =('times', 15, ' bold '))
                quitWindow.place(x = 420, y = 500)
                
                
                
            def teacher():
                window = tk.Tk()
                window.title("Teacher Entry Block")
                window.configure(background ='white')
                window.geometry("625x650")

                message = tk.Label(window, text ="Teacher Entry",bg ="green", fg = "white", width = 38,height = 3, font = ('times', 20, 'bold'))
                message.place(x =5, y = 5)
                
                lbl = tk.Label(window, text = "Enter Teacher Id :- ",
                width = 20, height = 2, fg ="green",
                bg = "white", font = ('times', 15, ' bold ') )
                lbl.place(x = 5, y = 190)

                txt = tk.Entry(window,
                width = 20, bg ="white",
                fg ="green", font = ('times', 15, ' bold '))
                txt.place(x = 230, y = 200)

                lbl2 = tk.Label(window, text ="Enter Teacher Name :-",
                width = 20, fg ="green", bg ="white",
                height = 2, font =('times', 15, ' bold '))
                lbl2.place(x = 5, y = 320)

                txt2 = tk.Entry(window, width = 20,
                bg ="white", fg ="green",
                font = ('times', 15, ' bold ') )
                txt2.place(x = 230, y = 330)
                
                def is_number(s):
                    try:
                        float(s)
                        return True
                    except ValueError:
                        pass

                    try:
                        import unicodedata
                        unicodedata.numeric(s)
                        return True
                    except (TypeError, ValueError):
                        pass

                    return False
                def TakeImages():	
                    
                    
                    Id =(txt.get())
                    name =(txt2.get())
                    
                
                    if(is_number(Id) and name.isalpha()):
                        
                        cam = cv2.VideoCapture(0)
                    
                        harcascadePath = "code/hdd/haarcascade_frontalface_default.xml"
                    
                        detector = cv2.CascadeClassifier(harcascadePath)
                    
                        sampleNum = 0
                        while(True):
                        
                            ret, img = cam.read()
                            
                            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                            
                            faces = detector.detectMultiScale(gray, 1.3, 5)
                            
                        
                            for (x, y, w, h) in faces:
                            
                                cv2.rectangle(img, (x, y), (
                                    x + w, y + h), (255, 0, 0), 2)
                                sampleNum = sampleNum + 1
                                
                                cv2.imwrite(
                                    "data_img/ "+name +"."+Id +'.'+ str(
                                        sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                            
                                cv2.imshow('frame', img)
                        
                            if cv2.waitKey(100) & 0xFF == ord('q'):
                                break
                            
                            elif sampleNum>60:
                                break
                    
                        cam.release()
                    
                        cv2.destroyAllWindows()
                    
                        res = "Images Saved for ID : " + Id +" Name : "+ name
                        
                        row = [Id, name]
                        with open('student_details/student_data.csv', 'a+') as csvFile:
                            writer = csv.writer(csvFile)
                        
                            writer.writerow(row)
                        csvFile.close()
                        message.configure(text = res)
                    else:
                        if(is_number(Id)):
                            res = "Enter Alphabetical Name"
                            message.configure(text = res)
                        if(name.isalpha()):
                            res = "Enter Numeric Id"
                            message.configure(text = res)

                
                def TrainImages():
                
                    recognizer = cv2.face.LBPHFaceRecognizer_create()
                    
                    harcascadePath = "code/hdd/haarcascade_frontalface_default.xml"
            
                    detector = cv2.CascadeClassifier(harcascadePath)
                
                    faces, Id = getImagesAndLabels("data_img")
                
                    recognizer.train(faces, np.array(Id))	
                    recognizer.save("TrainingLabelImage\Trainner.yml")
                
                    res = "Image Trained"
                    message.configure(text = res)

                def getImagesAndLabels(path):
                
                    imagePaths =[os.path.join(path, f) for f in os.listdir(path)]
                    faces =[]
                
                    Ids =[]
                
                    for imagePath in imagePaths:

                        pilImage = Image.open(imagePath).convert('L')
                        imageNp = np.array(pilImage, 'uint8')
                        Id = int(os.path.split(imagePath)[-1].split(".")[1])
                        faces.append(imageNp)
                        Ids.append(Id)	
                    return faces, Ids
                
                takeImg = tk.Button(window, text ="Take Images",command = TakeImages, fg ="white", bg ="green",
                width = 15, height = 3, activebackground = "Red",
                font =('times', 15, ' bold '))
                takeImg.place(x = 10, y = 500)

                trainImg = tk.Button(window, text ="Train Model",
                command = TrainImages, fg ="white", bg ="green",
                width = 15, height = 3, activebackground = "Red",
                font =('times', 15, ' bold '))
                trainImg.place(x = 215, y = 500)

            
                quitWindow = tk.Button(window, text ="Quit",
                command = window.destroy, fg ="white", bg ="green",
                width = 15, height = 3, activebackground = "Red",
                font =('times', 15, ' bold '))
                quitWindow.place(x = 420, y = 500)


                
                            
            
            

            


            takeImg = tk.Button(window, text ="Student Entry ",command = student, fg ="white", bg ="green",
            width = 15, height = 3, activebackground = "Red",
            font =('times', 15, ' bold '))
            takeImg.place(x = 215, y = 180)

            trainImg = tk.Button(window, text ="Teacher Entry",
            command = teacher, fg ="white", bg ="green",
            width = 15, height = 3, activebackground = "Red",
            font =('times', 15, ' bold '))
            trainImg.place(x = 215, y = 320)

        
            # quitWindow = tk.Button(window, text ="Quit",
            # command = window.destroy, fg ="white", bg ="green",
            # width = 15, height = 3, activebackground = "Red",
            # font =('times', 15, ' bold '))
            # quitWindow.place(x = 420, y = 500)


            

        newrecord = tk.Button(master, text="New Entry",command=openNewWindow,fg="black", bg="green"  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 18, 'italic bold '))
        newrecord.place(x=60, y=560)

        oldrecord = tk.Button(master, text="Entry Data",command=gate_cam_data,fg="black", bg="green"  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 18, 'italic bold '))
        oldrecord.place(x=320, y=560)

        unknownimages= tk.Button(master, text="Video Playlist",command=unknownimages,fg="black", bg="green"  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 18, 'italic bold '))
        unknownimages.place(x=580, y=560)

    

        def entrymark(name):
            
                with open('E:\col_project\entry_record.csv','r+') as f:
                    
                
                    mydatalist=f.readlines()
                    namelist=[]
                    idlist=[]
                    for line in mydatalist:
                        entry=line.split(',')
                        namelist.append(entry[0])
                    if name not in namelist:
                        now=datetime.now()
                            
                        tStr= now.strftime('%H:%M:%S')
                        dStr= now.strftime('%d/%m/%Y')
                        f.writelines(f'\n{name},{tStr},{dStr}')

                    
        
        while True:
            ret, img = cam.read()
            img = cv2.flip(img, 1) 

            

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            
            for(x, y, w, h) in faces:
                # cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
                Ids, conf = recognizer.predict(gray[y:y + h, x:x + w])								
                if(conf <= 65):
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    aa = df.loc[df['Ids'] == Ids]['faces'].values
            
                    tt = str(Ids)+","+aa
                    

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 2)
                    Ids =['Unknown']			
                    
                    aa= Ids
                    
                
                # if(conf > 66):
                #     noOfFile = len(os.listdir("Unknown_img_folder"))+1
                #     cv2.imwrite("Unknown_img_folder/Image"+
                #     str(noOfFile) + ".jpg", img[y:y + h, x:x + w])		
                # cv2.putText(img, str(*aa), (x, y + h),
                #     font, 1, (255, 255, 255), 2)
                x=str(*aa)
                entrymark(x)

            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img=ImageTk.PhotoImage(Image.fromarray(img))
            l1['image']=img
            
            master.update()
            
       
     
   
    project()
    

App()