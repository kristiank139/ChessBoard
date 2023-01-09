from tkinter import *

raam = Tk()
raam.title("Malelaud")

tahvel = Canvas(raam, width= 800, height=800, background="gray")
tahvel.create_line(40, 40, 760, 40, 760, 760, 40, 760, 40, 40)
tahvel.pack()
x = 0
y = 0
n = 0
rida = 0
i = 0
while n < 64:
    while rida < 8:
        if i == 0:
            tahvel.create_rectangle(40+x, 40+y, 130+x, 130+y, fill = "#000501")
            i += 1
        else:
            tahvel.create_rectangle(40+x, 40+y, 130+x, 130+y, fill = "#cbd6ce")
            i -= 1
        x += 90
        rida += 1
        n += 1
    if i == 1:
        i = 0
    else:
        i = 1
    x = 0
    y += 90
    rida = 0
        
    n += 1
print("Done")
    
    

raam.mainloop()
