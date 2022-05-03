import os
import time
import mouse
import random
from multiprocessing import Process
import pyautogui
from playsound import playsound
import tkinter as tk
import pyttsx3

isRunning = False
def Verification():
    global isRunning
    if input("Are you sure that you want to run the program(y/n):") == "y":
        print("Any damage caused to your pc(even tough there shouldn't be any) are not my responsability.")
        if input("Do you still want to proceed(y/n):") == "y":
            isRunning = True



firstStage = 20
step = 0


def talk():
    engine = pyttsx3.init()

    voice_num = 0
    text_to_say = "Your pc is now mine you motherfucker I will shove my dick in your ass I will shove my dick in your ass I will shove my dick in your ass I will shove my dick in your ass.I will shove my dick in your ass I will shove my dick in your ass I will shove my dick in your ass I will shove my dick in your ass I will shove my dick in your ass"


    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_num].id)

    engine.say(text_to_say)
    engine.runAndWait()

    root = tk.Tk()
    root.title(str(':):):):):):)'))
    root.geometry("300x300")

    label = tk.Label(root, text=str('HAHAHAHAHA C just une blague'))
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(root, text="OKAY", command = root.destroy)
    B1.pack()

    root.mainloop()

def mouseGlitch():
    nbrMove = 1000
    while True:
        xMove = random.randint(-300, 300)
        yMove = random.randint(-300, 300)
        mouse.move(xMove, yMove)
        nbrMove -=1
        time.sleep(0.005)

def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()

def rickroll():
    while isRunning:
        playsound('Rick_Roll')
        time.sleep(10)

def popupmsg():  
    root = tk.Tk()
    root.title(str('WARNING'))
    root.geometry("300x300")

    label = tk.Label(root, text=str('You have been contaminateds'))
    label.pack(side="top", fill="both", pady=10)
    B1 = tk.Button(root, text="Okay", command = root.destroy)
    B1.pack()

    root.mainloop()

    root = tk.Tk()
    root.title(str('WARNING'))
    root.geometry("300x300")

    label = tk.Label(root, text=str('Starting desinfection'))
    label.pack(side="top", fill="both", pady=10)
    B1 = tk.Button(root, text="Okay", command = root.destroy)
    B1.pack()

    root.mainloop()


    root = tk.Tk()
    root.title(str('WARNING'))
    root.geometry("300x300")

    label = tk.Label(root, text=str('desenfection failed'))
    label.pack(side="top", fill="both", pady=10)
    B1 = tk.Button(root, text="Okay", command = root.destroy)
    B1.pack()

    root.mainloop()


    root = tk.Tk()
    root.title(str('WARNING'))
    root.geometry("300x300")

    label = tk.Label(root, text=str("It's too late, your pc has been completely corrupted"))
    label.pack(side="top", fill="both", pady=10)
    B1 = tk.Button(root, text="Okay", command = root.destroy)
    B1.pack()

    root.mainloop()

    root = tk.Tk()
    root.title(str('&*@(_@|?}|'))
    root.geometry("300x300")

    label = tk.Label(root, text=str('*(@)(@)?"}:@*&'))
    label.pack(side="top", fill="both", pady=10)
    B1 = tk.Button(root, text=")(O>:k3#a:>?y", command = root.destroy)
    B1.pack()

    root.mainloop()

    runInParallel(talk, mouseGlitch)

def spam():
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
    pyautogui.press('enter')
    pyautogui.write("VIRUS!")
 
def write():
    global step
    time.sleep(10)
    os.startfile('notepad.exe')
    time.sleep(3)
    pyautogui.write("Bonjour", interval=0.05)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.write("Comment va tu", interval=0.05)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.write("Votre pc semble comporter un virus...", interval=0.05)
    pyautogui.press('enter')  
    runInParallel(spam, popupmsg)


def counter():
    global firstStage
    global isRunning
    while True:
        if(firstStage > 0):
            time.sleep(1)
            firstStage-=1
        else:
            isRunning = False
            break

if __name__ == '__main__':
    Verification()
    if(isRunning):
        print("Starting the virus...")
        runInParallel(counter, write)
    else:
        print("Ok, have a nice day")
    
    