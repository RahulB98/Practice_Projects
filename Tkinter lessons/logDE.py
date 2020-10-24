x = [7,21]
length = int(x[0])
width = int(x[1])

for i in range(0,length):
    if i < int((length/2)):
        des1 = int(2*i+1)
        des2 = int((width-(des1*3))/2)
        print(des2*"-" + des1*".|." + des2*"-")
    elif i == int((length/2)):
        des2 = int((width-7)/2)
        print(des2*"-" + "WELCOME" + des2*"-")

for j in range(int((length/2))-1,-1,-1):
    des1 = int(2*j+1)
    des2 = int((width-(des1*3))/2)
    print(des2*"-" + des1*".|." + des2*"-")