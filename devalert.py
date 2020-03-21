import win10toast

tost = win10toast.ToastNotifier()

import time, threading
print("""*****************************

    Developer Exercise

             
             BY : 53DEV
             

*****************************""")

    
StartTime=time.time()


def action() :
    print('Geçen Süre : {:.1f}s'.format(time.time()-StartTime))
    show = tost.show_toast('Egzersiz zamanı', 'Bilgisayar başında hareketsiz 40 Dakika geçirdiniz. \n En az 5 dakika egzersiz yapınız  ', duration=10)
        


class setInterval :
    def __init__(self,interval,action) :
        self.interval=interval
        self.action=action
        self.stopEvent=threading.Event()
        thread=threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self) :
        nextTime=time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()) :
            nextTime+=self.interval
            self.action()

    def cancel(self) :
        self.stopEvent.set()

# start action every 0.6s
inter=setInterval(2400,action)
print('Program başladı! \n 40 dakika sonra seni uyaracağız: {:.1f}s'.format(time.time()-StartTime))



# will stop interval in 5s
t=threading.Timer(68.400,inter.cancel)
t.start()