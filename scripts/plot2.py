#!/home/chenyuan/anaconda3/envs/py36/bin/python
import os
import re
import sys
import matplotlib.pyplot as plt

def readTxt(filename):
    with open(filename, "r", encoding="utf-8") as file:
        ListX=[]
        ListY=[]
        ListZ=[]
        MinY=1000
        MinZ=1000
        for line in file:
            if re.search('Iteration',line):
                s = line.split(' ')
                #print(s)
                if s.count("loss"):
                    x = int(s[5])
                    ListX.append(x)
                #    y = float(s[12])
                #    ListY.append(y)
            if re.search('#0',line):
                s = line.split(' ')
                #print(s)
                y = float(s[14])
                if y<MinY:
                    MinY=y
                ListY.append(MinY)
            if re.search('#1',line):
                s = line.split(' ')
                #print(s)
                z = float(s[14])
                if z<MinZ:
                    MinZ=z
                ListZ.append(MinZ)
    return ListX,ListY,ListZ


if __name__ == '__main__':
    #os.chdir(sys.path[0])
    env_dist=os.environ
    #print(env_dist.get('PWD'))
    os.chdir(env_dist.get('PWD'))
    txtFile = "results.txt"

    x,y,z = readTxt(txtFile)

    plt.subplot(211)
    plt.xlabel('iterations')
    plt.ylabel('loss')
    plt.axis([10000, x[len(x)-1]+10000, 0, 0.1])
    #plt.scatter(x, y)
    plt.plot(x, z)
    plt.subplot(212)
    plt.xlabel('iterations')
    plt.ylabel('loss')
    plt.axis([10000, x[len(x)-1]+10000, 0, 200])
    plt.plot(x, y)

    plt.show()
