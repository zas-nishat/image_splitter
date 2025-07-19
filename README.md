# 🖼️ Image Splitter (Batch Desktop EXE Tool)

**Image Splitter** is a simple desktop application (Python-based, `.exe` ready) that splits all images in a selected folder into two vertical halves — left and right.  
You can share the `.exe` file with anyone — no Python or installation required.

---

## 💾 EXE Version (No Python Needed)

✅ If you're using the **`.exe` version** (`batch_image_splitter.exe`):

1. Just **double-click the `.exe` file**.
2. Select the folder containing your images.
3. The app will create a folder called `split_output` inside that folder.
4. All split images (`page1_left.jpg`, `page1_right.jpg`, ...) will be saved there.
5. No installation needed, just run and use!

---

## 🛠️ Features

- Select a folder containing multiple images.
- Automatically splits each image **vertically into left and right halves**.
- Saves output with sequential page names:
  - `page1_left.jpg`, `page1_right.jpg`
  - `page2_left.jpg`, `page2_right.jpg`
  - ...
- Automatically creates `split_output` folder inside the selected folder.
- Supports: `.jpg`, `.jpeg`, `.png`, `.bmp`
- Maintains **natural order sorting** (`image2.jpg` comes before `image10.jpg`).
- Converts output to **monochrome (black & white)**.

---

## 💻 Requirements (for Python version)

> Skip this if you're using the `.exe` file

- Python 3.x (tested with Python 3.7+)
- Pillow (Python Imaging Library)
- Tkinter (comes with Python by default)

---

## 🧪 Installation (Python users only)

1. Install Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Install required library:

```bash
pip install pillow
