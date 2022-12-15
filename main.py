import tkinter as tk

buttons = ['soap', 'bleach', 'disinfectant', 'broom', 'mop', 'rags', 'tissue ', 'masks', 'gloves']
btnElements = []

def handleBtnClick(btnText):
    btnElements[buttons.index(btnText)]["background"] = "green"


    with open("choices.txt", 'a+') as f:
        f.write(btnText + "\r\n")


master = tk.Tk()




tk.Label(master, text="Mark if missing :").grid(row=0)
tk.Label(master, text="Mark if missing :").grid(row=1)
tk.Label(master, text="Mark if missing :").grid(row=2)
tk.Label(master, text="Mark if missing :").grid(row=3)
tk.Label(master, text="Mark if missing :").grid(row=4)
tk.Label(master, text="Mark if missing :").grid(row=5)
tk.Label(master, text="Mark if missing :").grid(row=6)
tk.Label(master, text="Mark if missing :").grid(row=7)
tk.Label(master, text="Mark if missing :").grid(row=8)

for i, z in enumerate(buttons):
    btnElements.append(tk.Button(master, text=z,width=12 ,command=lambda ztemp=z: handleBtnClick(ztemp)))
    btnElements[i].grid(
        row=i,
        column=2,
        sticky=tk.W)

tk.Button(master,
          text='Order Confirmation',
          command=master.quit).grid(row=10,
                                    column=1,
                                    sticky=tk.W,)


tk.mainloop()