import tkinter as tk
import string
from random import choices

def window(self):
    self.title("Gen pwd By Astartes")
    self.resizable(False,False)
    self.geometry("360x100")
    element(self)  
    self.mainloop() 
def element(self):
    global output
    output = tk.Text(self,width=42,height=1)
    output.place(x=12,y=25)
    tk.Label(self, text="Clave Generada").place(x=10,y=0)
    tk.Button(self, text="Generar",command=brain).place(x=12,y=70)
    tk.Button(self, text="Limpiar",command=clear).place(x=80,y=70)
def clear():
    return output.delete("1.0","end")
def brain():
        character = string.ascii_letters + string.digits + string.punctuation
        pwd = ''.join(choices(character, k=40))
        return output.insert(tk.END,pwd)

if __name__ == "__main__":
    window(tk.Tk())