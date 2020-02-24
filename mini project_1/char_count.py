import tkinter as tk
def charcount():
    output.delete(0.0,"end")
    w=inputUser.get(0.0,"end")
    sp=decision.get()
    c=0
    if sp==1:
        for k in w:
            if k=="\n":
                continue
            c=c+1
    elif sp==2:
        for k in w:
            if k==" " or k=="\n":
                continue
            c=c+1

    output.insert(tk.INSERT,c)
window=tk.Tk()
window.title("Count Characters")
window.geometry("500x600")
label=tk.Label(window,text="Input")
inputUser=tk.Text(window,width=450,height=10,font=("Helvetica",16),wrap="word")
decision=tk.IntVar()
r1=tk.Radiobutton(window,text="with spaces",value=1,variable=decision)
r2=tk.Radiobutton(window,text="without spaces",value=2,variable=decision)
button=tk.Button(window,text="Count the number of characters",command=charcount)
label2=tk.Label(window,text="number of characters")
output=tk.Text(window,width=20,height=2,font=("Helvetica",16),wrap="word")

label.pack()
inputUser.pack()
r1.pack()
r2.pack()
label2.pack()
output.pack()
button.pack()

window.mainloop()