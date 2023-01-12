import tkinter as tk
import os
from PIL import Image, ImageTk, ImageEnhance
from glob import glob
import pandas as pd
import time
from collections import OrderedDict

PHOTO_ROOT = "data"


class SimpleLogging:
    def __int__(self):
        self.left = 0
        self.right = 0


class MainDisplayApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Eye Image Quality")
        self.root.geometry("300x150")
        self.frame = tk.Frame(self.root)
        self.label_left = tk.Label(self.root)
        self.label_right = tk.Label(self.root)
        self.log_file = dict()
        self.image_structure = OrderedDict()
        self.construct_log_file()
        self.construct_structure()
        self.current_displayed_image_num = -1
        self.current_displayed_image_person = -1
        self.initial_display_image()

    def construct_log_file(self):
        sub_directories = os.listdir(PHOTO_ROOT)
        for i in sub_directories:
            person_num = int(i)
            self.log_file[person_num] = dict()
            sub_images = os.listdir(os.path.join(PHOTO_ROOT, i, 'Left'))
            for j in sub_images:
                j = j.split('.')[0]
                self.log_file[person_num][int(j)] = SimpleLogging()

    def construct_structure(self):
        sub_directories = os.listdir(PHOTO_ROOT)
        for i in sub_directories:
            folder_queue = []
            sub_images = os.listdir(os.path.join(PHOTO_ROOT, i, 'Left'))
            for j in sub_images:
                j = j.split('.')[0]
                folder_queue.append(int(j))
            self.image_structure[int(i)] = folder_queue

    def initial_display_image(self):
        self.current_displayed_image_person = list(self.image_structure.keys())[0]
        self.current_displayed_image_num = self.image_structure[self.current_displayed_image_person].pop(0)
        left_img, right_img = self.acquire_image()

        self.label_left.grid(row=2, column=1)
        self.label_left.image = left_img
        self.label_left['image'] = left_img
        self.label_right.grid(row=3, column=1)
        self.label_right.image = right_img
        self.label_right['image'] = right_img
        self.add_button_to_frame()


    def add_button_to_frame(self):
        lg = tk.Button(self.root, text="Left Good", command=self.lg_callback)
        lm = tk.Button(self.root, text="Left Mid", command=self.lm_callback)
        lb = tk.Button(self.root, text="Left Bad", command=self.lb_callback)
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
        self.log_file[self.current_displayed_image_person][self.current_displayed_image_num].left = 3
        self.update_image()

    def lm_callback(self):
        self.log_file[self.current_displayed_image_person][self.current_displayed_image_num].left = 2
        self.update_image()

    def lb_callback(self):
        self.log_file[self.current_displayed_image_person][self.current_displayed_image_num].left = 1
        self.update_image()

    def rg_callback(self):
        self.log_file[self.current_displayed_image_person][self.current_displayed_image_num].right = 3
        self.update_image()

    def rm_callback(self):
        self.log_file[self.current_displayed_image_person][self.current_displayed_image_num].right = 2
        self.update_image()

    def rb_callback(self):
        self.log_file[self.current_displayed_image_person][self.current_displayed_image_num].right = 1
        self.update_image()

    def update_image(self):
        image_remaining_list = self.image_structure[self.current_displayed_image_person]

        if len(image_remaining_list) > 0:
            # Continue to the next image with the same person if there still exist images not displayed
            self.current_displayed_image_num = self.image_structure[self.current_displayed_image_person].pop(0)
        else:
            # Move on to a new person and delete the old one
            del self.image_structure[self.current_displayed_image_person]
            if len(list(self.image_structure.keys())) > 0:
                self.current_displayed_image_person = list(self.image_structure.keys())[0]
                self.current_displayed_image_num = self.image_structure[self.current_displayed_image_person].pop(0)
            else:
                # Exist if all has been displayed
                self.root.destroy()
                return

        left_img, right_img = self.acquire_image()
        self.label_left.config(image=left_img)
        self.label_left.image = left_img
        self.label_right.config(image=right_img)
        self.label_right.image = right_img

    def acquire_image(self):
        left_full_path = os.path.join(PHOTO_ROOT, '{:03d}'.format(self.current_displayed_image_person), 'Left',
                                      '{}.png'.format(self.current_displayed_image_num))

        right_full_path = os.path.join(PHOTO_ROOT, '{:03d}'.format(self.current_displayed_image_person), 'Right',
                                       '{}.png'.format(self.current_displayed_image_num))

        left_img = Image.open(left_full_path)
        right_img = Image.open(right_full_path)
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
        return left_img, right_img


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = MainDisplayApp()
    test.display()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
