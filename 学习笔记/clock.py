# 这是一个关于时间的简单程序，它会显示当前时间，并每秒钟更新一次。
# 导入必要的模块
from time import time, localtime, sleep
# 定义时钟类
class Clock(object):

    def __init__(self,hour=0,minute=0,second=0):
        
        self._hour=hour
        self._minute=minute
        self._second=second
 
   # 类方法：获取当前时间
    @classmethod   
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    
    # 运行时钟
    def run(self):
        
        self._second+=1
        if self._second==60:
            self._second=0
            self._minute+=1
            if self._minute==60:
                self._minute=0
                self._hour+=1
                if self._hour==24:
                    self._hour=0

    # 显示时间
    def show(self):
        return "%02d:%02d:%02d" %(self._hour,self._minute,self._second)
    
# 主函数
def main():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

# 运行程序
if __name__ == "__main__":
    main()


