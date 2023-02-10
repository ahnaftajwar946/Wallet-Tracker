# Import module 
from tkinter import *
from PIL import ImageTk,Image
  
# Create object 
root = Tk()
root.title("Title")
  
# Adjust size 
root.geometry("640x640")
root.configure(background="black")

class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("/Users/ahnaftajwar/Downloads/moneyimg.png")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

e = Example(root)
e.pack(fill=BOTH, expand=YES)


  
# Add image file
#bg = PhotoImage(file = "/Users/ahnaftajwar/Downloads/money2.png")
#bg = ImageTk.PhotoImage(Image.open("/Users/ahnaftajwar/Downloads/moneyimg.png"))
  
# Show image using label
#label1 = Label( root, image = bg)
#label1.place(x = 0, y = 0)
  
label2 = Label( root, text = "Welcome")
label2.pack(pady = 50)
  
# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 20 )
  
# Add buttons
button1 = Button(root,text="Exit")
button1.pack(pady=20)
  
button2 = Button(root, text = "Start")
button2.pack(pady = 20)
  
button3 = Button(root, text = "Reset")
button3.pack(pady = 20)


# Execute tkinter
root.mainloop()