from margin import getMargin
import convert
import os

def similarity(left,right):
    black=0
    sum=0
    for i in range(len(left)):
        if(left[i]==255 and right[i]==255):
            pass
        else:
            if(left[i]==0 and right[i]==0):
                black=black+1;
            sum=sum+1
    if(black==0 and sum==0):
        return 0.4
    return float(black)/float(sum)
number=1
files=os.listdir(convert.outpaths[number])
margindata={}
similaritydata={}
for i in range(len(files)):
    leftdata=getMargin(convert.outpaths[number]+"\\"+files[i],1)
    rightdata=getMargin(convert.outpaths[number]+"\\"+files[i],2)
    margindata[(i,1)]=leftdata
    margindata[(i,2)]=rightdata
for i in range(len(files)):
    for j in range(len(files)):
        simvalue=similarity(margindata[(i,2)],margindata[(j,1)])
        similaritydata[(i,j,1)]=simvalue
        similaritydata[(j,i,2)]=simvalue
print(similaritydata[(6,8,1)])
list=range(len(files))
list.remove(0)
current=0
sequence=[]
sequence.append(0)
while(len(list)!=0):
    max=0
    next=0
    for i in range(len(list)):
        if(similaritydata[(current,list[i],1)]>max):
            next=i
            max=similaritydata[(current,list[i],1)]
    if(max>0.42):
        next=list[next]
        list.remove(next)
        sequence.append(next)
        current=next
    else:
        break
current=0
while(len(list)!=0):
    max=0
    next=0;
    for i in range(len(list)):
        if(similaritydata[(current,list[i],2)]>max):
            next=i
            max=similaritydata[(current,list[i],2)]
    next=list[next]
    list.remove(next)
    sequence.insert(0,next)
    current=next
print(sequence)
