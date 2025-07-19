import os
from tkinter import Tk, Button, Label, filedialog, messagebox
from PIL import Image

def split_image(path, save_folder):
    img = Image.open(path)
    width, height = img.size
    
    # Split vertically in the middle
    left_box = (0, 0, width // 2, height)
    right_box = (width // 2, 0, width, height)
    
    left_part = img.crop(left_box)
    right_part = img.crop(right_box)
    
    base_name = os.path.splitext(os.path.basename(path))[0]
    
    left_part.save(os.path.join(save_folder, f"{base_name}_part1.jpg"))
    right_part.save(os.path.join(save_folder, f"{base_name}_part2.jpg"))

def select_images():
    file_paths = filedialog.askopenfilenames(
        title="Select images", 
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if not file_paths:
        return
    
    save_folder = filedialog.askdirectory(title="Select folder to save split images")
    if not save_folder:
        return
    
    for path in file_paths:
        split_image(path, save_folder)
    
    messagebox.showinfo("Done", f"Split {len(file_paths)} image(s) successfully!")

def main():
    root = Tk()
    root.title("Simple Image Splitter")
    root.geometry("300x150")

    label = Label(root, text="Split images into 2 parts (vertical)", pady=10)
    label.pack()

    btn_select = Button(root, text="Select Images and Split", command=select_images)
    btn_select.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
