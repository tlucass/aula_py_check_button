from tkinter import *

def muda_imagem():
    if shoutmon.get() and ballistamon.get() and dorulumon.get():
        nova_imagem = "./digimons/shoutmonX5.png"
        imagem["file"] = nova_imagem
    elif shoutmon.get() and ballistamon.get():
        nova_imagem = "./digimons/shoutmonX2.png"
        imagem["file"] = nova_imagem
    elif shoutmon.get() and dorulumon.get():
        nova_imagem = "./digimons/shoutmonX3.png"
        imagem["file"] = nova_imagem
    elif ballistamon.get() and dorulumon.get():
        nova_imagem = "./digimons/shoutmonX4.png"
        imagem["file"] = nova_imagem
    elif shoutmon.get():
        nova_imagem = "./digimons/shoutmon.png"
        imagem["file"] = nova_imagem
    elif ballistamon.get():
        nova_imagem = "./digimons/ballistamon.png"
        imagem["file"] = nova_imagem
    elif dorulumon.get():
        nova_imagem = "./digimons/dorulumon.png"
        imagem["file"] = nova_imagem
    else:
        nova_imagem = "./digimons/desconhecido.png"
        imagem["file"] = nova_imagem



window = Tk()
window.title("O Programa da Fusão")
window.geometry("700x500")

ballistamon = BooleanVar()
dorulumon = BooleanVar()
shoutmon = BooleanVar()

container1 = Frame(window)
container2 = Frame(window)
container1.pack(side=LEFT, padx=50)
container2.pack(pady=100)

check_ballistamon = Checkbutton(container1, text="Ballistamon", variable=ballistamon, command=muda_imagem)
check_dorulumon = Checkbutton(container1, text="Dorulumon", variable=dorulumon, command=muda_imagem)
check_shoutmon = Checkbutton(container1, text="Shoutmon", variable=shoutmon, command=muda_imagem)

check_ballistamon.grid(row=0, column=0)
check_dorulumon.grid(row=1, column=0)
check_shoutmon.grid(row=2, column=0)



imagem = PhotoImage(file="./digimons/desconhecido.png")
imagemDesconhecido = Label(container2)
imagemDesconhecido["image"] = imagem
imagemDesconhecido.pack()


window.mainloop()