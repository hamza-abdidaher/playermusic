import tkinter as tk 
import os 
import fnmatch
from pygame import mixer

canvas=tk.Tk()
canvas.title("hamza musik")
canvas.geometry("500x500")
canvas.config(bg= 'white')

rootpath ="C:\\Users\hamza\Downloads\demo"
pattern= "*.mp3"

mixer.init()

prec_img=tk.PhotoImage(file="prec.png")
play_img=tk.PhotoImage(file="play.png")
stop_img=tk.PhotoImage(file="stop.png")
pause_img=tk.PhotoImage(file="pause.png")
suiv_img=tk.PhotoImage(file="suiv.png")

def select():
    label.config(text=listbox.get("anchor"))
    mixer.music.load(rootpath+"\\"+listbox.get("anchor"))
    mixer.music.play()
    
def stop_and_restart_music():
    mixer.music.stop()
    listbox.select_clear('active')
    play_music()


listbox=tk.Listbox(canvas, fg="cyan", bg="black",width=100, font=('poppin',14))
listbox.pack(padx=15, pady=15)

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listbox.insert('end', filename)
        
label= tk.Label(canvas, text="", bg="white", fg='red', font=("poppin", 18)) 
label.pack(pady=15) 

top=tk.Frame(canvas, bg="white")
top.pack (padx= 10, pady=5, anchor='center')

precbutton= tk.Button(canvas, text="prec", image=prec_img, bg="white", borderwidth=0) 
precbutton.pack(pady=15, in_=top, side="left")  

pausebutton= tk.Button(canvas, text="pause", image=pause_img, bg="white", borderwidth=0,command=stop_and_restart_music) 
pausebutton.pack(pady=15, in_=top, side="left") 

playbutton= tk.Button(canvas, text="play", image=play_img, bg="white", borderwidth=0, command=select) 
playbutton.pack(pady=15, in_=top, side="left")  

stopbutton= tk.Button(canvas, text="stop", image=stop_img, bg="white", borderwidth=0) 
stopbutton.pack(pady=15, in_=top, side="left")  

suivbutton= tk.Button(canvas, text="suiv", image=suiv_img, bg="white", borderwidth=0) 
suivbutton.pack(pady=15, in_=top, side="left")  

        
        
        
        
        

canvas.mainloop()