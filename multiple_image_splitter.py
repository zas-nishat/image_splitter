import os
import re
from tkinter import Tk, Button, Label, filedialog, messagebox
from PIL import Image

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def split_image_with_page_number(path, save_folder, page_num):
    try:
        img = Image.open(path)
        width, height = img.size
        
        left_box = (0, 0, width // 2, height)
        right_box = (width // 2, 0, width, height)
        
        left_part = img.crop(left_box)
        right_part = img.crop(right_box)
        
        left_part.save(os.path.join(save_folder, f"page{page_num}_left.jpg"))
        right_part.save(os.path.join(save_folder, f"page{page_num}_right.jpg"))
    except Exception as e:
        print(f"Error processing {path}: {e}")

def select_folder_and_split_serial_auto_save():
    folder_path = filedialog.askdirectory(title="Select folder with images to split")
    if not folder_path:
        return
    
    # Auto create subfolder named 'split_output' inside the selected folder
    save_folder = os.path.join(folder_path, "split_output")
    os.makedirs(save_folder, exist_ok=True)
    
    supported_ext = ('.jpg', '.jpeg', '.png', '.bmp')
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(supported_ext)]
    files.sort(key=natural_sort_key)
    
    image_files = [os.path.join(folder_path, f) for f in files]
    
    if not image_files:
        messagebox.showwarning("No images found", "No supported images found in the selected folder.")
        return
    
    total = len(image_files)
    for i, img_path in enumerate(image_files, 1):
        split_image_with_page_number(img_path, save_folder, i)
        print(f"Processed {i} / {total}: {img_path}")
    
    messagebox.showinfo("Done", f"Split {total} images successfully!\nSaved in:\n{save_folder}")

def main():
    root = Tk()
    root.title("Batch Image Splitter (Auto Save)")
    root.geometry("450x150")

    label = Label(root, text="Split images and auto-save in 'split_output' folder", pady=10)
    label.pack()

    btn_folder = Button(root, text="Select Folder and Split Images", command=select_folder_and_split_serial_auto_save)
    btn_folder.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
