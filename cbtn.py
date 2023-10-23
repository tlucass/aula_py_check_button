from tkinter import *

def verifica_pertences():
    mensagem = "Seus Pertences"
    if tv.get():
        mensagem += "\n" + check_tv["text"]
    if pc.get():
        mensagem += "\n" + check_pc["text"]
    if vg.get():
        mensagem += "\n" + check_vg["text"]
    if bk.get():
        mensagem += "\n" + check_bk["text"]
    rotulo1["text"] =  mensagem

window = Tk()
window.title("Pesquisa")
window.geometry("400x200")
tv = BooleanVar()
pc = BooleanVar()
vg = BooleanVar()
bk = BooleanVar()
container1 = Frame(window)
container2 = Frame(window)
container1.pack(side=LEFT)
container2.pack(side=TOP)

check_tv = Checkbutton(container1, text="Televisão", variable=tv, width=15, padx=10, pady=5, anchor="w", command=verifica_pertences)

check_pc = Checkbutton(container1, text="PC", variable=pc, width=15, padx=10, pady=5, anchor="w", command=verifica_pertences)

check_vg = Checkbutton(container1, text="Video-Game", variable=vg, width=15, padx=10, pady=5, anchor="w", command=verifica_pertences)

check_bk = Checkbutton(container1, text="Bicicleta", variable=bk, width=15, padx=10, pady=5, anchor="w", command=verifica_pertences)

check_tv.grid(row=0, column=0)
check_pc.grid(row=1, column=0)
check_vg.grid(row=2, column=0)
check_bk.grid(row=3, column=0)

rotulo1 = Label(container2, text="Seus pertences:", padx=20)
rotulo1["font"] = ("Arial", "14", "bold")
rotulo1.grid(row=0, column=1)

window.mainloop()


