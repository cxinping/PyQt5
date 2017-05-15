# -*- coding: utf-8 -*-
 
class MyCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def __privateCountFun(self):
        print('这是私有方法')
        self.__secretCount += 1
        self.publicCount += 1
        #print (self.__secretCount)
        
    def publicCountFun(self):
        print('这是公共方法')
        self.__privateCountFun()

if __name__ == "__main__":
    counter = MyCounter()
    counter.publicCountFun()
    counter.publicCountFun()
    print ('instance publicCount=%d' % counter.publicCount)
    print ('Class publicCount=%d' % MyCounter.publicCount)
    
    # 报错，实例不能访问私有变量
    # print (counter.__secretCount)  
    # 报错，实例不能访问私有方法
    # counter.__privateCountFun()