#!/home/chenyuan/anaconda3/envs/py36/bin/python
import os
import re
import sys
import matplotlib.pyplot as plt

def readTxt(filename):
    with open(filename, "r", encoding="utf-8") as file:
        ListX=[]
        ListY=[]
        MinY=10
        for line in file:
            s = line.find("")
            #print(line)
            if re.search('Iteration',line):
                s = line.split(' ')
                if s.count("loss"):
                    x = int(s[5])
                    ListX.append(x)
                    y = float(s[12])
                    if y<MinY:
                        MinY=y
                    ListY.append(MinY)
    return ListX,ListY


if __name__ == '__main__':
    os.chdir(sys.path[0])
    txtFile = "results.txt"

    x,y = readTxt(txtFile)

    plt.subplot(211)
    plt.xlabel('iterations')
    plt.ylabel('loss')
    plt.axis([x[len(x)-1]-1000, x[len(x)-1]+50, 0, 0.1])
    plt.scatter(x, y)
#    print(sum(y[len(y)-1000:])/1000)
    plt.subplot(212)
    plt.xlabel('iterations')
    plt.ylabel('loss')
    plt.plot(x, y)

    plt.show()
