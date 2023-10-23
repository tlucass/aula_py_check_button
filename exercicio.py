from tkinter import *

def muda_imagem():
    mensagem = "Seus Pertences"
    if ballistamon.get():
        nova_imagem = "./digimons/ballistamon.png"
        imagemDesconhecido["file"] = nova_imagem
    elif check_dorulomon.get():
        nova_imagem = "./digimons/dorulomon.png"
        imagemDesconhecido["file"] = nova_imagem
    elif shoutmon.get():
        nova_imagem = "./digimons/shoutmon.png"
        imagemDesconhecido["file"] = nova_imagem
    elif shoutmon.get() and ballistamon.get():
        nova_imagem = "./digimons/shoutmonX2.png"
        imagemDesconhecido["file"] = nova_imagem
    elif shoutmon.get() and dorulomon.get():
        nova_imagem = "./digimons/shoutmonX3.png"
        imagemDesconhecido["file"] = nova_imagem
    elif ballistamon.get() and dorulomon.get():
        nova_imagem = "./digimons/shoutmonX4.png"
        imagemDesconhecido["file"] = nova_imagem
    else:
        nova_imagem = "./digimons/shoutmonX5.png"
        imagemDesconhecido["file"] = nova_imagem

    

window = Tk()
window.title("O Programa da Fusão")
window.geometry("700x500")

ballistamon = BooleanVar()
dorulomon = BooleanVar()
shoutmon = BooleanVar()

container1 = Frame(window)
container2 = Frame(window)
container1.pack(side=LEFT)
container2.pack(side=TOP)

check_ballistamon = Checkbutton(container1, text="Ballistamon", variable=ballistamon, width=15, padx=10, pady=5, anchor="w", command=muda_imagem)

check_dorulomon = Checkbutton(container1, text="Dorulomon", variable=dorulomon, width=15, padx=10, pady=5, anchor="w", command=muda_imagem)

check_shoutmon = Checkbutton(container1, text="Shoutmon", variable=shoutmon, width=15, padx=10, pady=5, anchor="w", command=muda_imagem)

check_ballistamon.grid(row=0, column=0)
check_dorulomon.grid(row=1, column=0)
check_shoutmon.grid(row=2, column=0)



imagem = PhotoImage(file="./digimons/desconhecido.png")
imagemDesconhecido = Label(container2)
imagemDesconhecido["image"] = imagem
imagemDesconhecido.pack()




window.mainloop()