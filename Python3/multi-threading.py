import threading
import time
import queue
import os

#Don't call your file threading.py!!
class myThread(threading.Thread):

   # This is a thread! 
   def __init__(self, threadID, name, delay):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.delay = delay

   # Once a thread object is created, its activity must be started by calling the thread’s start() method.
   # This invokes the run() method in a separate thread of control.
   def run(self):
      print("Starting " + self.name)
      print_time(self.name, 5, self.delay)
      print("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      time.sleep(delay)
      print(threadName + " " + str(time.ctime(time.time())))
      counter -= 1

# Create new threads, one waits 2 seconds to print, the other waits one.
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
#thread1.start()
#thread2.start()



# #Don't call your file threading.py!!
# class myThreadFileWrite(threading.Thread):

#    # This is a thread! 
#    def __init__(self, threadID, name, delay):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.delay = delay

#    # Once a thread object is created, its activity must be started by calling the thread’s start() method.
#    # This invokes the run() method in a separate thread of control.
#    def run(self):
#       print("Starting " + self.name)
#       print_time(self.name, 5, self.delay)
#       print("Exiting " + self.name)

# def print_time(threadName, counter, delay):
#    # This will allow for a full file but thow an error when trying to move it
#    #file = open("threading.txt", "a+")
#    while counter:
#       time.sleep(delay)
#       # Here will allow the file rename but we end up with an incomplete file
#       file = open("threading.txt", "a+")
#       file.write(threadName + " " + str(time.ctime(time.time())) + "\n")
#       print(threadName + " " + str(time.ctime(time.time())))
#       counter -= 1
#       # Here will allow the file rename but we end up with an incomplete file
#       file.close()
#    # This will allow for a full file but thow an error when trying to move it
#    #file.close()

#    try:
#       os.rename("threading.txt", "threading_done.txt")
#    except FileExistsError:
#       os.remove("threading_done.txt")
#       os.rename("threading.txt", "threading_done.txt")


# # Create new threads, one waits 2 seconds to print, the other waits one.
# thread1 = myThreadFileWrite(1, "Thread-1", 1)
# thread2 = myThreadFileWrite(2, "Thread-2", 2)

# # Start new Threads
# thread1.start()
# thread2.start()


exitFlag = 0 

class myThreadLocking(threading.Thread):

   # This is a thread! 
   def __init__(self, threadID, name, dataQueue):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.dataQueue = dataQueue

   # Once a thread object is created, its activity must be started by calling the thread’s start() method.
   # This invokes the run() method in a separate thread of control.
   def run(self):
      print("Starting " + self.name)
      process_data(self.name, self.dataQueue)
      print("Exiting " + self.name)

def process_data(threadName, dataQueue):

   while not exitFlag:
      lock.acquire()
      if not dataQueue.empty():
         data = dataQueue.get()
         # Prevent competing threads accessing the data for 5 seconds
         time.sleep(5)
         lock.release()
         print(threadName + " processed this data! " + str(data))
      else:
         lock.release()
      time.sleep(1)
 

lock = threading.Lock()

data = range(1,100)
dataQueue = queue.Queue(100)

for number in data:
   dataQueue.put(number)

# Create new threads
thread1 = myThreadLocking(1, "Thread-1", dataQueue)
thread2 = myThreadLocking(2, "Thread-2", dataQueue)
thread3 = myThreadLocking(3, "Thread-3", dataQueue)
thread4 = myThreadLocking(4, "Thread-4", dataQueue)
thread5 = myThreadLocking(5, "Thread-5", dataQueue)
thread6 = myThreadLocking(6, "Thread-6", dataQueue)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()

while not dataQueue.empty():
   pass

exitFlag = 1

print ("----VS---")

data = range(1,20)
dataQueue = queue.Queue(20)

for number in data:
   dataQueue.put(number)

while not dataQueue.empty():
   data = dataQueue.get()
   time.sleep(1)  
   print("processed this data on a single thread! " + str(data))
 
