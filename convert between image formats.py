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

img = cv2.imread(input_path)

if img is None:
    print(f"Error: Could not find or open the image at: {input_path}")
    exit()

folder_path = filedialog.asksaveasfilename(
    title = "Save your converted image",
    defaultextension = ".png",
    filetypes=[
        ("*.bmp", "Windows Bitmap"),
        ("*.dib", "Device Independent Bitmap"),
        ("*.hdr", "Radiance High Dynamic Range"),
        ("*.jp2", "JPEG 2000 Image"),
        ("*.jpeg", "JPEG Image"),
        ("*.jpg", "JPEG Image"),
        ("*.pbm", "Portable Pixmap (Binary)"),
        ("*.pgm", "Portable Graymap"),
        ("*.pic", "Softimage PIC Image"),
        ("*.png", "Portable Network Graphics"),
        ("*.ppm", "Portable Pixmap (Color)"),
        ("*.pxm", "Pixel Map Image"),
        ("*.ras", "Sun Raster Graphic"),
        ("*.sr", "Sony Raw Image"),
        ("*.tif", "Tagged Image File Format"),
        ("*.tiff", "Tagged Image File Format"),
        ("*.webp", "WebP Image")
    ]
)
if folder_path:
    print(folder_path)
    output_path = folder_path
cv2.imwrite(output_path, img)
print(f"Successfully inverted image and saved to: {output_path}")