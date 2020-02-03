import multiprocessing
import threading
import time


class wrk1(multiprocessing.Process):
    def __init__(self):
        print "wrk1::run init"
        multiprocessing.Process.__init__(self)
    def run(self):
    	print "wrk1::run start"
        while True:
            print "wrk1::run run"
            time.sleep(1)
        print "wrk1::run ended"

class wrk2(threading.Thread):
    def __init__(self):
        self.stop=False
        print "wrk2::run init"
        threading.Thread.__init__(self)
    def setStop(self):
        self.stop=True
    def run(self):
    	print "wrk2::run start"
        while not self.stop:
            print "wrk2::run run"
            time.sleep(1)
        print "wrk2::run ended"



if __name__ == '__main__':
    print "main::wrk1 start"
    w1 = wrk1()
    #sp.daemon = True
    w1.start()
    print "main::wrk1 started "
    time.sleep(3)
    print "main::wrk1 send-terminate"
    w1.terminate()
    print "main::wrk1 end"

    print "==================="

    print "main::wrk2 start"
    w2 = wrk2()
    w2.start()
    print "main::wrk2 started "
    time.sleep(3)
    print "main::wrk2 send-terminate"
    w2.setStop()
    print "main::wrk2 end"
