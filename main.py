import tkinter as tk
import os
from PIL import Image, ImageTk, ImageEnhance
from glob import glob
import time

PHOTO_ROOT = "data"


class MainDisplayApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Eye Image Quality")
        self.root.geometry("300x150")
        self.frame = tk.Frame(self.root)
        self.label_left = tk.Label(self.root)
        self.label_right = tk.Label(self.root)
        self.log_file = None

    def construct_log_file(self):

    def display_image(self):
        all_directories = os.listdir(PHOTO_ROOT)
        for i in all_directories:
            self.display_image_in_dir(os.path.join(PHOTO_ROOT, i))

    def display_image_in_dir(self, dir):
        left_dir = os.path.join(dir, 'Left')
        right_dir = os.path.join(dir, 'Right')
        for img_names in glob(os.path.join(left_dir, "*.png")):
            full_path = os.path.normpath(img_names)
            img_number = full_path.split(os.sep)[-1]
            left_img_path = os.path.join(left_dir, img_number)
            right_img_path = os.path.join(right_dir, img_number)
            left_img = Image.open(left_img_path)
            right_img = Image.open(right_img_path)
            # Perform necessary image manipulation if necessary
            left_img = ImageEnhance.Contrast(left_img)
            left_img = left_img.enhance(4.0)
            left_img = left_img.resize((90, 54))
            right_img = ImageEnhance.Contrast(right_img)
            right_img = right_img.enhance(4.0)
            right_img = right_img.resize((90, 54))
            # End image manipulation
            left_img = ImageTk.PhotoImage(left_img)
            right_img = ImageTk.PhotoImage(right_img)
            self.label_left.grid(row=2, column=1)
            self.label_left.image = left_img
            self.label_left['image'] = left_img
            self.label_right.grid(row=3, column=1)
            self.label_right.image = right_img
            self.label_right['image'] = right_img
            self.add_button_to_frame()

            img_number = int(img_number.split('.')[0])

    def add_button_to_frame(self):
        lg = tk.Button(self.root, text="Left Good")
        lm = tk.Button(self.root, text="Left Mid")
        lb = tk.Button(self.root, text="Left Bad")
        rg = tk.Button(self.root, text="Right Good")
        rm = tk.Button(self.root, text="Right Mid")
        rb = tk.Button(self.root, text="Right Bad")
        lg.grid(row=2, column=2)
        lm.grid(row=2, column=3)
        lb.grid(row=2, column=4)
        rg.grid(row=3, column=2)
        rm.grid(row=3, column=3)
        rb.grid(row=3, column=4)

    def display(self):
        self.root.mainloop()

    def lg_callback(self):



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = MainDisplayApp()
    test.display_image()
    test.display()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
