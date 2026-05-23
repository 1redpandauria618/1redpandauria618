import qrcode
from qrcode.constants import ERROR_CORRECT_M
import os

def make_qr(url: str, filename: str = "qrcode.png", box_size: int = 10, border: int = 4):
    """
    Generate a QR code image from a URL (including long links).
    Saves it into the /images folder inside the project root (qr).
    """

    # Path to the images folder inside the project root
    project_root = os.getcwd()          # this is your 'qr' folder
    images_folder = os.path.join(project_root, "images")
    os.makedirs(images_folder, exist_ok=True)

    save_path = os.path.join(images_folder, filename)

    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)

    print(f"Saved QR code to {save_path}")

if __name__ == "__main__":
    long_link = "https://parlourgardens.nablabcn.com/project9.html"
    make_qr(long_link, "peter-stutchbury.png")
