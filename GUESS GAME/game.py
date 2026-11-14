from tkinter import *
from tkinter import messagebox
import tkinter as tk
from random import randint
import random

def rounded_button(canvas,x1,y1,x2,y2,text,command,outcolor="#00B4D8",incolor="#00E5FF",text_color="#FFFFFF"):
    radius = 50
    points = [x1+radius,y1,x2-radius,y1,x2,y1,x2,y1+radius,x2,y2-radius,x2,y2,x2-radius,y2,x1+radius,y2,x1,y2,x1,y2-radius,x1,y1+radius,x1,y1]
    button = canvas.create_polygon(points,smooth=True,splinesteps=24,fill=outcolor,outline=outcolor)
    label = canvas.create_text((x1 + x2) / 2,(y1 + y2) / 2,text=text,fill=text_color,font=("Segoe UI", 12, "bold"))
    canvas.tag_bind(button,"<Button-1>",lambda event:command())
    canvas.tag_bind(label,"<Button-1>",lambda event:command())
    canvas.tag_bind(button,"<Enter>",lambda event:canvas.itemconfig(button,fill=incolor))
    canvas.tag_bind(label,"<Enter>",lambda event:canvas.itemconfig(button,fill=incolor))
    canvas.tag_bind(button,"<Leave>",lambda event:canvas.itemconfig(button,fill=outcolor))
    canvas.tag_bind(label,"<Leave>",lambda event:canvas.itemconfig(button,fill=outcolor))
class game:
    def __init__(self,first_number,last_number,guesses):
        self.firstnum=first_number
        self.lastnum=last_number
        self.guesses=guesses
        self.remaining_guesses=self.guesses
        self.number=random.randint(first_number,last_number)
        self.matchs_result=[]
        self.attempts=0
        self.highest_score=0
        self.root=tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW",lambda:None)
        self.root.withdraw()
        self.root.title(f"{first_number}-{last_number} WINDOW")
        self.root.configure(bg="#0B1020")
        self.root.resizable(width=False,height=False)
        self.root.geometry("400x400")
    def run(self):
        self.root.deiconify()
        self.matchs_result.clear()
        for widget in self.root.winfo_children():
            widget.destroy()
        Label(self.root,text="guess the number",bg="#0B1020",fg="#00E5F0",font=("Segoe UI",14,"bold")).pack()
        guess=StringVar(self.root)
        Entry(self.root,textvariable=guess,bg="#191D30",fg="#FFFFFF",insertbackground="#00E5F0",font=("Segoe UI",16),justify="center",relief="flat",highlightthickness=2,highlightbackground="#00E5F0",highlightcolor="#B026FF").pack()
        score=0
        score_label=Label(self.root,text=f"score:{score}",bg="#0B1020",fg="#00E5F0",font=("Segoe UI",14,"bold"))
        score_label.pack()
        result_label=Label(self.root,text="",bg="#0B1020",fg="#00E5F0",font=("Segoe UI",14,"bold"))
        result_label.pack()
        remaining_label=Label(self.root,text=f"remaings:{self.remaining_guesses}",bg="#0B1020",fg="#00E5F0",font=("Segoe UI",14,"bold"))
        remaining_label.pack()
        def check_results():
            self.number=random.randint(self.firstnum,self.lastnum)
            nonlocal score
            result=guess.get()
            if not result.isdigit():
                messagebox.showerror("ERROR","ENTER A NUMBER")
                return None
            if result.isdigit() and int(result)<self.firstnum or int(result)>self.lastnum:
                messagebox.showerror("ERROR",f"NUMBER MUST BE BETWEEN {self.firstnum} TILL {self.lastnum}")
                return None
            if result.isdigit() and int(result)==self.number:
                score+=(self.attempts)+1
                score_label.config(text=f"score:{score}")
                result_label.config(text="you hit the target",fg="green")
                if not self.remaining_guesses==0:
                    self.remaining_guesses-=1
                remaining_label.config(text=f"remainigs:{self.remaining_guesses}")
                return True
            else:
                if score>=1:
                    score-=1
                score_label.config(text=f"score:{score}")
                result_label.config(text=f"not found.number was {self.number}",fg="red")
                if not self.remaining_guesses==0:
                    self.remaining_guesses-=1
                remaining_label.config(text=f"remainigs:{self.remaining_guesses}")
                return False
        
        
                
        def check():
            checkresult=check_results()

            if checkresult is not None:
                self.matchs_result.append(checkresult)
                print(self.matchs_result)
                

            if self.remaining_guesses==0:
                
                self.attempts+=1
                for widget in self.root.winfo_children():
                    widget.destroy()
                if score>self.highest_score:
                    self.highest_score=score
                self.remaining_guesses=self.guesses
                if self.matchs_result.count(True)>((len(self.matchs_result))/2):
                    Label(self.root,text="YOU WIN",bg="#0B1020",fg="#00F024",font=("Segoe UI",14,"bold")).pack()
                    playagain_canvas=Canvas(self.root,width=200,height=60,bg="#0B1020",highlightthickness=0)
                    playagain_canvas.pack(pady=10)
                    rounded_button(playagain_canvas,10,0.10,190,55,"PLAY AGAIN",lambda:([widget.destroy() for widget in self.root.winfo_children()],self.run()))
                    exit_canvas=Canvas(self.root,width=200,height=60,bg="#0B1020",highlightthickness=0)
                    exit_canvas.pack(pady=10)
                    rounded_button(exit_canvas,10,0.10,190,55,"EXIT",lambda:(self.root.withdraw(),[widget.destroy() for widget in self.root.winfo_children()]))
                    return
                else:
                    Label(self.root,text="YOU LOSE",bg="#0B1020",fg="#F03000",font=("Segoe UI",14,"bold")).pack()
                    playagain_canvas=Canvas(self.root,width=200,height=60,bg="#0B1020",highlightthickness=0)
                    playagain_canvas.pack(pady=10)
                    rounded_button(playagain_canvas,10,0.10,190,55,"PLAY AGAIN",lambda:([widget.destroy() for widget in self.root.winfo_children()],self.run()))
                    exit_canvas=Canvas(self.root,width=200,height=60,bg="#0B1020",highlightthickness=0)
                    exit_canvas.pack(pady=10)
                    rounded_button(exit_canvas,10,0.10,190,55,"EXIT",lambda:(self.root.withdraw(),[widget.destroy() for widget in self.root.winfo_children()]))
                    return

                
                
                
        #button=Button(self.root,text="guess",command=check,bg="#00BFCB",fg="#FFFFFF",activebackground="#B026FF",activeforeground="#FFFFFF",font=("Segoe UI",13,"bold"),relief="flat",bd=0,cursor="hand2",highlightthickness=2,highlightbackground="#00E5F0")
        #button.pack()
        #button.bind("<Enter>",lambda event: button.configure(bg="#B026FF"))
        #button.bind("<Leave>",lambda event: button.configure(bg="#00BFCB"))
        canvas=Canvas(self.root,width=200,height=60,bg="#0B1020",highlightthickness=0)
        canvas.pack(pady=10)
        rounded_button(canvas,10,0.10,190,55,"GUESS",check)
        self.root.mainloop()
    def close(self):
        self.root.destroy()

