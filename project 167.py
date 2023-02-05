from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Working on Canvas Using Functions")
root.geometry("600x600")


color_label=Label(root, text="Choose a Color:")
color_label.place(relx=0.7,rely=0.9,anchor=CENTER) 

color_label=Label(root, text="endy:")
color_label.place(relx=0.7,rely=0.8,anchor=CENTER) 

color_label=Label(root, text="endx:")
color_label.place(relx=0.5,rely=0.8,anchor=CENTER) 

color_label=Label(root, text="starty:")
color_label.place(relx=0.3,rely=0.8,anchor=CENTER) 

color_label=Label(root, text="startx:")
color_label.place(relx=0.1,rely=0.8,anchor=CENTER)

Chooseacolor = ["red","yellow","blue","black","purple","orange","green","grey"]
selectdeval = StringVar()
dropdown = ttk.Combobox(root, values=Chooseacolor, textvariable=selectdeval)
dropdown.place(relx=0.8,rely=0.9,anchor=CENTER)

canvas=Canvas(root, width = 1000, height=510, bg="white", highlightbackground="lightgray")
canvas.pack()

endx = ["50","100","150","200","250","300","350","400","450","500","550","600"]
selectdeval = StringVar()
dropdown = ttk.Combobox(root, values=endx, textvariable=selectdeval)
dropdown.place(relx=0.6,rely=0.8,anchor=CENTER) 

starty = ["50","100","150","200","250","300","350","400","450","500","550","600"]
selectdeval = StringVar()
dropdown = ttk.Combobox(root, values=starty, textvariable=selectdeval)
dropdown.place(relx=0.4,rely=0.8,anchor=CENTER)  

input_box = Entry(root)
input_box.insert(0, "black")
input_box.place(relx=0.8,rely=0.7, anchor = CENTER)

startx = ["50","100","150","200","250","300","350","400","450","500","550","600"]
selectdeval = StringVar()
dropdown = ttk.Combobox(root, values=startx, textvariable=selectdeval)
dropdown.place(relx=0.2,rely=0.8,anchor=CENTER) 

endy = ["50","100","150","200","250","300","350","400","450","500","550","600"]
selectdeval = StringVar()
dropdown = ttk.Combobox(root, values=endy, textvariable=selectdeval)
dropdown.place(relx=0.8,rely=0.8,anchor=CENTER)

img=ImageTk.PhotoImage(Image.open ("start_point1.png"))
my_image = canvas.create_image(50,50,image=img)

keypress = ""
oldx=50
oldy=50
newx=50
newy=50

def line(event): 
    oldx = startx.get() 
    oldy = starty.get() 
    newx = endx.get() 
    newy = endy.get()
    keypress = "l"
    color = Chooseacolor.get()
    draw(keypress, oldx, oldy, newx, newy)  
    
def circle(event):
    oldx = startx.get() 
    oldy = starty.get() 
    newx = endx.get() 
    newy = endy.get()
    keypress = "c"
    color = Chooseacolor.get()
    draw(keypress, oldx, oldy, newx, newy)   

def rectangle(event):
    oldx = startx.get() 
    oldy = starty.get() 
    newx = endx.get() 
    newy = endy.get()
    keypress = "r"
    color = Chooseacolor.get()
    draw(keypress, oldx, oldy, newx, newy)

def draw(  keypress, oldx, oldy, newx, newy):
        fill_color = dropdown.get() 
        if (keypress == "c"): 
            draw_circle= canvas.create_oval(oldx,oldy,newx,newy,width = 3, fill= fill_color)
        if (keypress == "r"): 
            draw_rectangle= canvas.create_rectangle(oldx,oldy,newx,newy,width = 3,fill= fill_color)  
        if (keypress == "l"): 
            draw_line= canvas.create_line(oldx,oldy,newx,newy,width = 3, fill= fill_color) 
            
def right_dir(event):
    global keypress  
    global oldx 
    global oldy 
    global newx 
    global newy 
    oldx = newx 
    oldy = newy 
    newx=newx+5 
    keypress  = "right" 
    draw(keypress , oldx, oldy, newx, newy)
    
def left_dir(event):
    global keypress  
    global oldx 
    global oldy 
    global newx 
    global newy 
    oldx = newx 
    oldy = newy 
    newx=newx-5 
    direction = "left" 
    draw(keypress , oldx, oldy, newx, newy)  

def up_dir(event):
    global keypress  
    global oldx 
    global oldy 
    global newx 
    global newy 
    oldx = newx 
    oldy = newy 
    newy=newy-5 
    direction = "up" 
    draw(keypress , oldx, oldy, newx, newy)
    
def down_dir(event):
    global keypress 
    global oldx 
    global oldy 
    global newx 
    global newy 
    oldx = newx 
    oldy = newy 
    newy=newy+5 
    keypress  = "down" 
    draw(keypress , oldx, oldy, newx, newy) 

def draw(  keypress , oldx, oldy, newx, newy):
        fill_color = input_box.get() 
        if (keypress  == "right"): 
            right_line= canvas.create_line(oldx,oldy,newx,newy,width = 3,fill= fill_color)
        if (keypress == "left"): 
            left_line= canvas.create_line(oldx,oldy,newx,newy,width = 3,fill= fill_color)  
        if (keypress  == "up"): 
            up_line= canvas.create_line(oldx,oldy,newx,newy,width = 3,fill= fill_color)
        if (keypress  == "down"): 
            down_line= canvas.create_line(oldx,oldy,newx,newy,width = 3,fill= fill_color) 
            
root.bind("<Right>",right_dir) 
root.bind("<Left>",left_dir)
root.bind("<Down>",down_dir) 
root.bind("<Up>",up_dir)
root.bind("<c>",circle) 
root.bind("<r>",rectangle)
root.bind("<l>",line) 

root.mainloop()