# image_splitter

# Batch Image Splitter
This is a simple Python desktop application to split all images in a selected folder into two vertical parts (left and right). The split images are saved automatically inside a subfolder named split_output within the selected folder.

# Features
Select a folder containing images.

Automatically split each image vertically into two parts: left and right.

# Output images are saved with sequential page numbering:

page1_left.jpg, page1_right.jpg

page2_left.jpg, page2_right.jpg

and so on...

Automatically creates a split_output folder inside the selected folder and saves all output images there.

# Supports image formats: .jpg, .jpeg, .png, .bmp.

Sorts input images in natural order, so files like image2.jpg come before image10.jpg.

# Requirements
Python 3.x installed (tested with Python 3.7+)

Pillow library for image processing

Tkinter library for GUI (usually comes bundled with Python)

# Installation
Install Python:
Download and install Python from python.org.

# Install Pillow library:
Open a terminal or command prompt and run:

pip install pillow
# How to Use
Save the script multiple_image_splitter.py in a folder on your computer for multiple images.

Open a terminal or command prompt and navigate to the folder containing the script.

# Run the script with:

python multiple_image_splitter.py
# A window titled "Image Splitter (Auto Save)" will open.

Click the Select Folder and Split Images button.

Choose the folder containing the images you want to split.

The program will create a split_output folder inside the selected folder and save the split images there.

After processing, a popup message will show the total number of images processed and the output folder path.

# Output Files
For each image in the input folder, two images are created:

pageN_left.jpg — left half of the Nth image

pageN_right.jpg — right half of the Nth image

N corresponds to the image's order in the sorted list.

# Troubleshooting
Make sure Python and Pillow are properly installed.

If the program doesn’t open a window, verify Tkinter is installed and working.

Supported image formats: .jpg, .jpeg, .png, .bmp only.

Large batches of images may take some time to process.

