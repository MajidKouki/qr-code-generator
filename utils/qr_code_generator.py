# Initial imports
import qrcode, qrcode.image.svg
import os
import sys

# Uses user data to create QR code
def qr_code_generator(qr_data, filename_data):
    # Pathing to properly save QR codes to 'imgs' directory
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, "..", "imgs", filename_data)
    iterate_path = os.path.join(dirname, "..", "imgs")

    # Iterate through 'imgs' to find duplicates before attemtping to create new file
    for file in os.listdir(iterate_path):
        if file == filename_data:
            sys.exit("Error: Duplicate file")

    # Save QR code depending on file type
    if ".svg" in filename_data:      
        img = qrcode.make(qr_data, image_factory = qrcode.image.svg.SvgImage)
        type(img)
        img.save(filepath)
    else:
        img = qrcode.make(qr_data)
        type(img)
        img.save(filepath)
                

