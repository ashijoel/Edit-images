import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
import cv2
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()
pixelAmount = 0
percent = 0
file_path = filedialog.askopenfilename(
    title="Select your image",
    filetypes=[
        ("Image Files", "*.png *.jpg *.jpeg *.webp *.bmp *.tiff *.tif *.dib *.jp2 *.pbm *.pgm *.ppm *.pxm *.ras *.sr *.hdr *.pic"),
        ("All Files", "*.*")
    ]
)
if file_path:
    print(f"{file_path}")
    root_name, file_extension = os.path.splitext(file_path)
input_path = file_path
print(file_path)

# 1. Load the image ONCE into memory
img = cv2.imread(input_path)

if img is None:
    print(f"Error: Could not find or open the image at: {input_path}")
    exit()

height, width, channels = img.shape

# 2. Process all pixels entirely in RAM using your loop variables (y and x)
for y in range(height):
    for x in range(width):
        loadingBar = ""
        # Read the pixel using correct [y, x] matrix format
        b, g, r = img[y, x]
        
        # Calculate new inverted colors
        r_new = int(((r - 127.5) * -1) + 127.5)
        g_new = int(((g - 127.5) * -1) + 127.5)
        b_new = int(((b - 127.5) * -1) + 127.5)
        
        # Update the pixel in memory
        img[y, x] = [b_new, g_new, r_new]
        pixelAmount += 1
        if percent < round((pixelAmount / (height * width)) * 100):
            percent = round((pixelAmount / (height * width)) * 100)
            for a in(range(percent)):
                loadingBar = loadingBar + "="
            if len(str(percent)) == 1:
                spaces = "    "
            elif len(str(percent)) == 2:
                spaces = "   "
            else:
                spaces = "  "
            print(f"{percent}%{spaces}{loadingBar}>")

file_type = file_extension.lower()

folder_path = filedialog.asksaveasfilename(
    title = "Save your inverted image",
    defaultextension = file_type,
    filetypes=[
        ("PNG Image", "*.png"),
        ("JPEG Image", "*.jpg *.jpeg"),
        ("WebP Image", "*.webp"),
        ("Bitmap Image", "*.bmp *.dib"),
        ("TIFF Image", "*.tiff *.tif"),
        ("JPEG 2000 Image", "*.jp2"),
        ("Portable Pixmap / Map", "*.pbm *.pgm *.ppm *.pxm"),
        ("Sun Raster", "*.ras *.sr"),
        ("Radiance HDR", "*.hdr *.pic")
    ]
)
if folder_path:
    print(folder_path)
    output_path = folder_path
cv2.imwrite(output_path, img)
print(f"Successfully inverted image and saved to: {output_path}")