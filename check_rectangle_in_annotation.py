import pandas as pd
import os   
import numpy as np
import re
import shutil
imgPath = input("Image Source Path ==>>")+"/"
labelPath = input("Label Source Path ==>>")+"/"
# labelDest = input("Label Destination Path ==>>")+"/"
imgDest = "problem_item/"
labelDest = imgDest
labels = os.listdir('labels')
images = os.listdir('images')


import os

def check_and_create_folder(folder_path):
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' was created successfully.")
        except Exception as e:
            print(f"Error creating folder: {e}")
    else:
        print(f"Folder '{folder_path}' already exists.")
folder_path = 'problem_item'
check_and_create_folder(folder_path)



def is_perpendicular(v1, v2):
    return np.dot(v1, v2) == 0



xxx = {}
DDD = []
for data in labels:
    myData = labelPath+data
    if data.endswith('.txt'):
        with open(myData,'r') as ann:
            ant = []
            content = ann.read()
            all_content = content.split('\n')
            for annotation in all_content:
                myContent = annotation.split(' ')
                if len(myContent)==5:
                    ant.append(myContent)
            f = {myData:ant}
            if len(ant)>0:
                xxx[myData] = ant
                for i in range(1, len(ant) - 1):  
                    x1, y1 = float(ant[i-1][1]), float(ant[i-1][2])  
                    x2, y2 = float(ant[i][1]), float(ant[i][2])        
                    x3, y3 = float(ant[i+1][1]), float(ant[i+1][2])    
                    vector1 = np.array([x2 - x1, y2 - y1])
                    vector2 = np.array([x3 - x2, y3 - y2])
                    if not is_perpendicular(vector1, vector2):
                        break
                else:
                    DDD.append(f"{myData}==>>Contains Rectangles")
                    img = data.replace('.txt','.jpg')
                    if img in images:
                        shutil.copyfile(imgPath+img,imgDest+img)
                    shutil.copyfile(myData,labelDest+data)

print(f"DDD==>>{len(DDD)}") # || xxx==>>{len(xxx)}")


print(DDD)