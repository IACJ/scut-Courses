# -*- coding: utf-8 -*-

import numpy as np
import random
from collections import deque

def randomGenerateMatrix():
    '随机生成一个3*3的矩阵'
    temp = np.arange(9)
    random.shuffle(temp)
    return temp.reshape((3,3))


def BFS(Start,Target):
    '宽度优先搜索'
    
    print("初始状态为：")
    print (Start)
    print("目标状态为：")
    print (Target)
    print ()
    print ("宽度优先搜索中...")
    
    
    if (Start == Target).all():
        print ("初始状态与目标状态相同。")
        return
    RecordNum = 0
    totalSearch = 0
    Open = deque([(Start,0,RecordNum)]) # 状态、路径长度、记录号
    Record = list([(Start,-1)])         # 状态、上一步记录号
    Closed = set([Start.tostring()])
    
    
    while (Open):
        totalSearch += 1
        tempM,tempN,tempRecordNum = Open.popleft()
        if (totalSearch % 1000 == 0):
            print("总搜索次数:"+str(totalSearch)+",搜索路径长度:"+str(tempN)) 
        Px,Py = ( tempM.argmin()//3 , tempM.argmin() % 3)
        
        # 空格上移
        Px1,Py1 = Px-1,Py
        if (Px1 >= 0 ):
            M = tempM.copy()
            M[Px1][Py1],M[Px][Py] =  M[Px][Py],M[Px1][Py1]
            if (M == Target).all():
                print ("找到了，路径长度为"+str(tempN+1)+",路径如下")
                printPath(Record,tempRecordNum)
                print('最后一步:')
                print(M)
                print ("路径总长度为"+str(tempN+1))
                return True
            elif ( M.tostring() not in Closed):
                RecordNum +=1
                Open.append((M,tempN+1,RecordNum))
                Record.append((M,tempRecordNum))
                Closed.add(M.tostring())

            
        # 空格下移
        Px1,Py1 = Px+1,Py
        if (Px1 <= 2 ):
            M = tempM.copy()
            M[Px1][Py1],M[Px][Py] =  M[Px][Py],M[Px1][Py1]
            if (M == Target).all():
                print ("找到了，路径长度为"+str(tempN+1)+",路径如下")
                printPath(Record,tempRecordNum)
                print('最后一步:')
                print(M)
                print ("路径总长度为"+str(tempN+1))
                return True
            elif (M.tostring() not in Closed):
                RecordNum +=1
                Open.append((M,tempN+1,RecordNum))
                Record.append((M,tempRecordNum)  ) 
                Closed.add(M.tostring())
        
        # 空格左移
        Px1,Py1 = Px,Py-1
        if (Py1 >= 0 ):
            M = tempM.copy()
            M[Px1][Py1],M[Px][Py] =  M[Px][Py],M[Px1][Py1]
            if (M == Target).all():
                print ("找到了，路径长度为"+str(tempN+1)+",路径如下")
                printPath(Record,tempRecordNum)
                print('最后一步:')
                print(M)
                print ("路径总长度为"+str(tempN+1))
                return True
            elif (M.tostring() not in Closed):
                RecordNum +=1
                Open.append((M,tempN+1,RecordNum))
                Record.append((M,tempRecordNum))
                Closed.add(M.tostring())
            
        # 空格右移
        Px1,Py1 = Px,Py+1
        if (Py1 <= 2 ):
            M = tempM.copy()
            M[Px1][Py1],M[Px][Py] =  M[Px][Py],M[Px1][Py1]
            if (M == Target).all():
                print ("找到了，路径长度为"+str(tempN+1)+",路径如下")
                printPath(Record,tempRecordNum)
                print('最后一步:')
                print(M)
                print ("路径总长度为"+str(tempN+1))
                return True
            elif (M.tostring() not in Closed):
                RecordNum +=1
                Open.append((M,tempN+1,RecordNum))
                Record.append((M,tempRecordNum))
                Closed.add(M.tostring())
        
       
        
    print("搜索完毕，共搜索"+str(totalSearch)+"步，未找到可行解")
    return False

def printPath(Record,now):
    '递归打印路径'
    num = 0
    if (Record[now][1] != -1):
        num = printPath(Record,Record[now][1])
    else:
        print()
        print("初始状态:")
        print(Record[now][0])
        print()
        return 0
    num += 1
    print("第"+str(num)+"步:")
    print(Record[now][0])
    print()
    return num
    
    
if __name__ == "__main__":
    print ("欢迎带来8数码问题。")
    print ("0代表空格。")
    S = randomGenerateMatrix()
    T = randomGenerateMatrix()
    print ()
    testS =np.array([[2,8,3],
                     [1,6,4],
                     [7,0,5]])
        
    testT =np.array([[1,2,3],
                     [7,8,4],
                     [0,6,5]])
    if BFS(S,T):
        print()
        print("一个最优解如上所示")
        print("(其中第一行为开始状态，最后一行为目标状态，0代表空格)")
    else:
        print("无解")




