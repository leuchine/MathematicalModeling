from PIL import Image
#get the margin pixels of a picture,1 left 2 right 3 up 4 down
def getMargin(path,number):
    margin=[]
    img=Image.open(path)
    size=img.size
    data=img.getdata()
    if(number==1):
        for i in range(size[1]):
            margin.append(data[size[0]*i])
    elif(number==2):
        for i in range(size[1]):
            margin.append(data[size[0]*i+size[0]-1])
    elif(number==3):
        for i in range(size[0]):
            margin.append(data[i])
    else:
        for i in range(size[0]*(size[1]-1),len(data)):
            margin.append(data[i])
    return margin
