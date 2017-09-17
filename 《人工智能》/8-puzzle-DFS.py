# -*- coding: utf-8 -*-

import numpy as np
import random
from collections import deque

import sys



class DFS(object):
    def __init__ (self):
        '初始化'
        
        print ("欢迎带来8数码问题。")
        print ("0代表空格。")
        S = self.randomGenerateMatrix()
        T = self.randomGenerateMatrix()
        print ()
        testS =np.array([[2,8,3],
                         [1,6,4],
                         [7,0,5]])
        
        testT =np.array([[1,2,3],
                         [7,8,4],
                         [0,6,5]])
        self.Start = testS
        self.Target = testT
        print("初始状态为：")
        print (self.Start)
        print("目标状态为：")
        print (self.Target)
        print ()
        print ("深度优先搜索中...")      

    def randomGenerateMatrix(self):
        '随机生成一个3*3的矩阵'
        temp = np.arange(9)
        random.shuffle(temp)
        return temp.reshape((3,3))
    
    def run(self):
        '开始运行'
        
        if (self.Start == self.Target).all():
            print ("初始状态与目标状态相同。")
            return
        if self.run_DFS():
            print()
            print("一个最优解如上所示")
            print("(其中第一行为开始状态，最后一行为目标状态，0代表空格)")
        else:
            print("无解")
    
    def run_DFS(self): 
        
        RecordNum = 0
        totalSearch = 0
        Open = deque([(self.Start,0,RecordNum)]) # [(状态、路径长度、记录号)]
        Record = {self.Start.tostring():(0,'end')}         # {状态:(步数,上一状态)}
        
        while (Open):
            totalSearch += 1
            tempM,tempN,tempRecordNum = Open.popleft()
            if (totalSearch % 1000 == 0):
                #print("总搜索次数:"+str(totalSearch)+",搜索深度:"+str(tempN+1))
                print("总搜索次数:"+str(totalSearch))
            Px,Py = ( tempM.argmin()//3 , tempM.argmin() % 3)
        
            # 空格上移
            Px1,Py1 = Px-1,Py
            if (Px1 >= 0 ):
                M = tempM.copy()
                M[Px1][Py1],M[Px][Py] =  M[Px][Py],M[Px1][Py1]
                if (M == self.Target).all():
                    print ("找到了，路径长度为"+str(tempN+1)+",路径如下")
                    self.printPath(Record,tempM.tostring())
                    print('最后一步:')
                    print(M)
                    print ("路径总长度为"+str(tempN+1))
                    return True
                elif ( M.tostring() not in Record):
                    Open.appendleft((M,tempN+1,RecordNum))
                    Record[M.tostring()] = (tempN+1,tempM.tostring())
        

            
            # 空格下移
            Px1,Py1 = Px+1,Py
            if (Px1 <= 2 ):
                M = tempM.copy()
                M[Px1][Py1],M[Px][Py] =  M[Px][Py],M[Px1][Py1]
                if (M == self.Target).all():
                    print ("找到了，路径长度为"+str(tempN+1)+",路径如下")
                    self.printPath(Record,tempM.tostring())
                    print('最后一步:')
                    print(M)
                    print ("路径总长度为"+str(tempN+1))
                    return True
                elif ( M.tostring() not in Record):
                    Open.appendleft((M,tempN+1,RecordNum))
                    Record[M.tostring()] = (tempN+1,tempM.tostring())
        
            # 空格左移
            Px1,Py1 = Px,Py-1
            if (Py1 >= 0 ):
                M = tempM.copy()
                M[Px1][Py1],M[Px][Py] =  M[Px][Py],M[Px1][Py1]
                if (M == self.Target).all():
                    print ("找到了，路径长度为"+str(tempN+1)+",路径如下")
                    self.printPath(Record,tempM.tostring())
                    print('最后一步:')
                    print(M)
                    print ("路径总长度为"+str(tempN+1))
                    return True
                elif ( M.tostring() not in Record):
                    Open.appendleft((M,tempN+1,RecordNum))
                    Record[M.tostring()] = (tempN+1,tempM.tostring())
            
            # 空格右移
            Px1,Py1 = Px,Py+1
            if (Py1 <= 2 ):
                M = tempM.copy()
                M[Px1][Py1],M[Px][Py] =  M[Px][Py],M[Px1][Py1]
                if (M == self.Target).all():
                    print ("找到了，路径长度为"+str(tempN+1)+",路径如下")
                    self.printPath(Record,tempM.tostring())
                    print('最后一步:')
                    print(M)
                    print ("路径总长度为"+str(tempN+1))
                    return True
                elif ( M.tostring() not in Record):
                    Open.appendleft((M,tempN+1,RecordNum))
                    Record[M.tostring()] = (tempN+1,tempM.tostring())
    
        
        print("搜索完毕，未找到可行解")
        return False
    def printPath(self, Record,now):
        '递归打印路径'

        if (Record[now][1] != 'end'):
            num = self.printPath(Record,Record[now][1])
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
    # sys.setrecursionlimit(10000) #括号中的值为递归深度
    temp = DFS()
    temp.run()
 
