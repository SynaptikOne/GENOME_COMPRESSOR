# gui/splash_screen.py

#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licences/MIT
#------------------------------------------------------------------------------


import tkinter as tk
from PIL import Image, ImageTk




def show_splash(image_path, duration=3000):
    splash = tk.Tk()
    splash.overrideredirect(True)
    

    # Dimension recommandees : 800 x 400 (ratio 2:1)
    splash_width, splash_height = 800, 400



    # Centrage
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()

    
    x = (screen_width - splash_width) // 2
    y = (screen_height - splash_height) // 2


    splash.geometry(f"{splash_width}x{splash_height}+{x}+{y}")

    # Image + texte
    img = Image.open(image_path)
    img = img.resize((splash_width, splash_height), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)

    label_img = tk.Label(splash, image=photo)
    label_img.image = photo
    label_img.pack()

   


    splash.after(duration, splash.destroy)
    splash.mainloop()

if __name__ == "__main__":
    show_splash("splash/GENOME_COMPRESSOR_resized.png")

