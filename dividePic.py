from PIL import Image
import os

def dividePic(path):
    img=Image.open(path)
    size=img.size
    data=img.getdata()
    blacknum=[]
    for i in range(size[1]):
        margin=[]
        for j in range(size[0]):
            margin.append(data[size[0]*i+j])
        num=0
        for j in range(len(margin)):
            if margin[j]==0:
                num=num+1
        blacknum.append(num)
    #0 word 1 blank
    if(blacknum[0:1]==[0]):
        flag=1
    else:
        flag=0
    start=0
    linenum=0
    divide={0:[],1:[]}
    while(linenum<len(blacknum)):
        if(flag==0):
            while(blacknum[linenum:linenum+9]!=[0,0,0,0,0,0,0,0,0]):
                linenum=linenum+1
                if(linenum==len(blacknum)):
                    if(blacknum[linenum-1]==0):
                        linenum=linenum-1;
                        while(blacknum[linenum]==0):
                            linenum=linenum-1
                        divide[0].append((start,linenum))
                        divide[1].append((linenum+1,len(blacknum)-1))
                        return divide
                    divide[0].append((start,linenum-1))
                    return divide
            flag=1
            divide[0].append((start,linenum-1))
            start=linenum
        else:
            while(blacknum[linenum]==0):
                linenum=linenum+1
                if(linenum==len(blacknum)):
                    divide[1].append((start,linenum-1))
                    return divide
            flag=0
            divide[1].append((start,linenum-1))
            start=linenum
    return divide

def count():
    files=os.listdir("F:\\B\\33")
    ls=[]
    count=0
    for i in files:
        dict=dividePic("F:\\B\\33"+"\\"+i)
        ls.append(dict)
    dic={}
    for i in ls:
        num=dic.get((len(i[0]),len(i[1])),0)
        if((len(i[0]),len(i[1]))==(3,4)):
           print(count)
        dic[(len(i[0]),len(i[1]))]=num+1
        count=count+1
    return dic
print(count())
