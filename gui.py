# Importing necessary libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import numpy
import numpy as np
from tensorflow.keras.layers import Conv2D, Input


# Loading the Model
from keras.models import load_model
model = load_model('Age_Sex_Detection.h5')
# Initializing the GUI
top = tk.Tk()
top.geometry('800x600')  # Corrected typo here
top.title('Age & Gender Detector')
top.configure(background='#CDCDCD')

# Initializing the Labels (1 for Age & 1 for Sex)
label1 = Label(top, background="#CDCDCD", font=('arial', 15, "bold"))
label2 = Label(top, background="#CDCDCD", font=('arial', 15, 'bold'))
sign_image = Label(top)
# Defining Detect Function which detects age & gender of person in image using model
def Detect(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((48, 48))
    image = numpy.expand_dims(image, axis=0)
    image = np.delete(image, 0, 1)
    image = np.resize(image, (48, 48,3))
    print(image.shape)
    sex_f = ["Male", "Female"]
    image = np.array([image]) / 255
    pred = model.predict(image)
    age = int(np.round(pred[1][0]))
    sex = int(np.round(pred[0][0]))
    print("Predicted Age is" + str(age))
    print("predicted Gender is" + sex_f[sex])
    label1.configure(foreground="#011638", text=age)
    label2.configure(foreground="#011638", text=sex_f[sex])

# Defining show_Detect_button function
def show_Detect_button(file_path):
    Detect_b = Button(top, text="Detect Image", command=lambda: Detect(file_path), padx=10, pady=5)
    Detect_b.configure(background="#364156", foreground='white', font=('arial', 10, 'bold'))
    Detect_b.place(relx=0.79, rely=0.46)  # Corrected 'relax' to 'relx'

# Defining Upload Image Function
def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        label2.configure(text='')
        show_Detect_button(file_path)
  # Corrected passing file_path
    except:
        pass

upload = Button(top, text="Upload an Image", command=upload_image, padx=10, pady=5)
upload.configure(background="#364156", foreground='white', font=('arial', 10, 'bold'))  # Corrected color code
upload.pack(side='bottom',pady=50)  # Added this line to display the button
sign_image.pack(side='bottom',expand=True)
label1.pack(side="bottom", expand=True)  # Corrected 'size' to 'side'
label2.pack(side="bottom", expand=True)  # Corrected 'size' to 'side'
heading = Label(top, text="Age and Gender Detector", pady=20, font=('arial', 20, "bold"))
heading.configure(background="#CDCDCD", foreground="#364156")
heading.pack()
top.mainloop()  # Corrected 'mailloop' to 'mainloop'

