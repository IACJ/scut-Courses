# -*- coding: utf-8 -*-

import numpy as np
import random
from collections import deque

def randomGenerateMatrix():
    '随机生成一个3*3的矩阵'
    temp = np.arange(9)
    random.shuffle(temp)
    return temp.reshape((3,3))

def notIn(M,List):
    for index,value in enumerate(List):
        if (M == value[0]).all():
            return False
    return True

def BFS(Start,Target):
    '宽度优先搜索'
    if (Start == Target).all():
        print ("初始状态与目标状态相同。")
        return
    RecordNum = 0
    Open = deque([(Start,0,RecordNum)])
    Record = list([(Start,-1)])
    totalSearch =0
    
    
    while (Open and totalSearch<100000):
        totalSearch += 1
        tempM,tempN,tempRecordNum = Open.popleft()
        print("搜索路径长度:"+str(tempN)+",总搜索次数:"+str(totalSearch)) 
        Px,Py = ( tempM.argmin()//3 , tempM.argmin() % 3)
        
        # 空格上移
        Px1,Py1 = Px-1,Py
        if (Px1 >= 0 ):
            M = tempM.copy()
            M[Px1][Py1],M[Px][Py] =  M[Px][Py],M[Px1][Py1]
            if (M == Target).all():
                print ("找到了，路径长度为"+str(tempN+1)+",路径如下")
                printPath(Record,tempRecordNum)
                print(M)
                return True
            elif (notIn(M,Close)):
                RecordNum +=1
                Open.append((M,tempN+1,RecordNum))
                Record.append((M,tempRecordNum))

            
        # 空格下移
        Px1,Py1 = Px+1,Py
        if (Px1 <= 2 ):
            M = tempM.copy()
            M[Px1][Py1],M[Px][Py] =  M[Px][Py],M[Px1][Py1]
            if (M == Target).all():
                print ("找到了，路径长度为"+str(tempN+1)+",路径如下")
                printPath(Record,tempRecordNum)
                print(M)
                return True
            elif (notIn(M,Close)):
                RecordNum +=1
                Open.append((M,tempN+1,RecordNum))
                Record.append((M,tempRecordNum)  ) 
        
        # 空格左移
        Px1,Py1 = Px,Py-1
        if (Py1 >= 0 ):
            M = tempM.copy()
            M[Px1][Py1],M[Px][Py] =  M[Px][Py],M[Px1][Py1]
            if (M == Target).all():
                print ("找到了，路径长度为"+str(tempN+1)+",路径如下")
                printPath(Record,tempRecordNum)
                print(M)
                return True
            elif (notIn(M,Close)):
                RecordNum +=1
                Open.append((M,tempN+1,RecordNum))
                Record.append((M,tempRecordNum))
            
        # 空格右移
        Px1,Py1 = Px,Py+1
        if (Py1 <= 2 ):
            M = tempM.copy()
            M[Px1][Py1],M[Px][Py] =  M[Px][Py],M[Px1][Py1]
            if (M == Target).all():
                print ("找到了，路径长度为"+str(tempN+1)+",路径如下")
                printPath(Record,tempRecordNum)
                print(M)
                return True
            elif (notIn(M,Close)):
                RecordNum +=1
                Open.append((M,tempN+1,RecordNum))
                Record.append((M,tempRecordNum)    )  
        
        #print(str(tempRecordNum)+'and'+str(totalSearch))
        
    print("不找了，找不到的。")
    return False

def printPath(Record,now):
    '递归打印路径'
    if (Record[now][1] != -1):
        printPath(Record,Record[now][1])

    print(Record[now][0])
    print()
    return
    
    

print ("欢迎带来8数码问题。")
print ("0代表空格。")
S = randomGenerateMatrix()
T = randomGenerateMatrix()
print("初始状态为：")
print (S)
print("目标状态为：")
print (T)
print ()
print ("宽度优先搜索中...")
print ()

testS =np.array([[2,8,3],
                 [1,6,4],
                 [7,0,5]])
    
testT =np.array([[1,2,3],
                 [7,8,4],
                 [0,6,5]])
if BFS(testS,testT):
    print("(其中第一行为开始状态，最后一行为目标状态)")




