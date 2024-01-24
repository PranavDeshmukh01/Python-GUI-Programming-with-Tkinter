import tkinter 
import sys 
import time 

def onTime(): 
    print(time.ctime(time.time()))

def onExit(): 
    print("exiting...")
    sys.exit(0)

def main(): 
    
    root_window = tkinter.Tk() 
    root_window.title("Current TimeStamp")

    time_button = tkinter.Button(root_window)
    time_button.configure(text='Current TimeStamp', command=onTime)
    time_button.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)

    exit_button = tkinter.Button(root_window)
    exit_button.configure(text='Exit', command=onExit)
    exit_button.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)

    root_window.mainloop()

main()