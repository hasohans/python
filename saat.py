#python projesi 1 
#python ile dijital saat yapımı
from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title("SAAT")
window.geometry("600x200")
window.configure(bg="black")
window.resizable(False, False)

clock_label = Label(
    window, bg="black" , fg="cyan" ,font=("Arial",60,"bold"), relief="flat"
)
clock_label.place(x=20, y=20)

def update_label():
    current_time = strftime("%H: %M: %S\n %d-%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(160, uptade_label)
    clock_label.pack(anchor="center")


update_label()
window.mainloop()

#bitti
