from game import *
from game import game
from tkinter import *
import webbrowser

main=tk.Tk()
main.title("Main Menu")
main.configure(bg="#0B1020")
main.geometry("400x450")
Label(main,text="SEE MY OTHER PROJECTS \n BY CLICKING BUTTON BLOW:",bg="#0B1020",fg="#00E5F0",font=("Segoe UI",14,"bold")).pack()
def github_btn():
    webbrowser.open("https://github.com/0MORADI0")
    return
github_canvas=Canvas(main,width=200,height=60,bg="#0B1020",highlightthickness=0)
github_canvas.pack(pady=10)
easy_canvas=Canvas(main,width=200,height=60,bg="#0B1020",highlightthickness=0)
easy_canvas.pack(pady=10)
medium_canvas=Canvas(main,width=200,height=60,bg="#0B1020",highlightthickness=0)
medium_canvas.pack(pady=10)
hard_canvas=Canvas(main,width=200,height=60,bg="#0B1020",highlightthickness=0)
hard_canvas.pack(pady=10)

rounded_button(github_canvas,10,0.10,190,55,"CLICK HERE",github_btn,outcolor="#0B1020",text_color="#00F024")
easy=game(1,10,5)
rounded_button(easy_canvas,10,0.10,190,55,"EASY",easy.run)
medium=game(1,100,10)
rounded_button(medium_canvas,10,0.10,190,55,"MEDIUM",medium.run)
hard=game(1,1000,20)
rounded_button(hard_canvas,10,0.10,190,55,"HARD",hard.run)
main.protocol("WM_DELETE_WINDOW",lambda:(main.destroy(),easy.close(),medium.close(),hard.close()))

attempts_label=Label(main,text=f"attempts:0",bg="#0B1020",fg="#00E5F0",font=("Segoe UI",14,"bold"))
attempts_label.pack()
highest_score_label=Label(main,text="highest score:0",bg="#0B1020",fg="#00E5F0",font=("Segoe UI",14,"bold"))
highest_score_label.pack()
def update_attempts():
    attempts=easy.attempts+medium.attempts+hard.attempts
    attempts_label.config(text=f"attempts:{attempts}")
    if easy.highest_score>medium.highest_score and easy.highest_score>hard.highest_score:
        highest_score_label.config(text=f"highest score:0")
        highest_score_label.config(text=f"highest score:{easy.highest_score}")
    elif medium.highest_score>easy.highest_score and medium.highest_score>hard.highest_score:
        highest_score_label.config(text=f"highest score:0")
        highest_score_label.config(text=f"highest score:{medium.highest_score}")
    else:
        highest_score_label.config(text=f"highest score:0")
        highest_score_label.config(text=f"highest score:{hard.highest_score}")
    main.after(500,update_attempts)
    
    
update_attempts()

main.mainloop()