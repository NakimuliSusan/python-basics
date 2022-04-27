import  time

class stopwatch (time):
    def __init__(self,window) -> None:
        super().__init__(window)
        self.window = window
        self.new_time = ''
        self.running = False
        self.total_hours = 0
        self.total_minutes = 0
        self.total_seconds = 0
        self.pack()
        self.features()
def features (self) :
    self.stopwatch_label = time.Label(self,text="00:00:00",background="black",foreground="white",
    font=('arial',85,"italic"))
    self.stopwatch_label.pack()
    
     #we want the buttons to appear 
    self.start_timer_button = time.Button(self,text="START",height=5,width=7,font=('arial',19,"bold"),background="green")
    self.start_timer_button.pack(side=time.LEFT)

    self.stop_timer_button = time.Button(self,text="STOP",height=5,width=7,font=('arial',19,"bold"),background="red")
    self.stop_timer_button.pack(side=time.LEFT)

    self.reset_timer_button = time.Button(self,text="RESET",height=5,width=7,font=('arial',19,"bold"),background="yellow")
    self.reset_timer_button.pack(side=time.LEFT)

    self.quit_timer_button = time.Button(self,text="QUIT",height=5,width=7,font=('arial',19,"bold"),background="blue")
    self.quit_timer_button.pack(side=time.LEFT)

    self.window.title ("SUSAN'S STOP WATCH")

root= time.Tk()
obj =  stopwatch(
    window=root
)

obj.mainloop()