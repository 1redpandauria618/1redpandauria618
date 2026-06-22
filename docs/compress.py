from PIL import Image
import os

# Folder containing your images
folder = "images/folder"

# Max width/height (optional)
MAX_SIZE = 1600  # pixels

# JPEG quality (70–85 is ideal)
QUALITY = 75

for filename in os.listdir(folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join(folder, filename)

        img = Image.open(path)

        # Resize if too large
        img.thumbnail((MAX_SIZE, MAX_SIZE))

        # Overwrite the original file
        img.save(path, optimize=True, quality=QUALITY)

        print(f"Compressed: {filename}")
