import os
from PIL import Image
paths=["F:\\B\\1","F:\\B\\2","F:\\B\\3","F:\\B\\4","F:\\B\\5"]
outpaths=["F:\\B\\11","F:\\B\\22","F:\\B\\33","F:\\B\\44","F:\\B\\55"]
count=0
"""for i in paths:
    files=os.listdir(i)
    for j in files:
        print(j)
        img=Image.open(i+"\\"+j)
        img.convert("L").convert("1").save(outpaths[count]+"\\"+j)
    count=count+1"""   
