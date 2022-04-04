import time #import time module its a library in python

def time_comverter (sec): #convert seconds into minutes and minutes into hours by dividing by 60
    mins = sec  //60
    sec = sec % 60
    hours = mins //60
    mins = mins % 60
    print("Time elapsed = {0}:{1}:{2}:".format(int(hours),int(mins),sec))# it will print the time elapsed in this format 
    # hours,mins,sec

    input("Press Enter to start")#When Enter is pressed the start time is set using time.time()
    start_time = time.time()#seconds are passed since the watch was started.

    input("Press Enter to stop")#When the watch is stopped has number of seconds since the watch was stopped
    end_time = time.time()

    time_elapsed = end_time - start_time #To get the time elapsed we get the difference of end time and start time

    time_comverter(time_elapsed)#Then we convert the time elapsed into the format of hours,mins,sec
