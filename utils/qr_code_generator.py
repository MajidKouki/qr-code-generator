# Initial imports
import qrcode, qrcode.image.svg
import os

# Uses user data to create QR code
def qr_code_generator(qr_data, filename_data):
    # Pathing to properly save QR codes to 'imgs' directory
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, "..", "imgs", filename_data)

    # Iterate through files to find duplicates before attemtping to create new file
    for file in os.listdir(dirname):
        if file == filename_data:
            print("Error: Duplicate file")
        # Save QR code depending on file type
        if ".svg" in filename_data:      
            img = qrcode.make(qr_data, image_factory = qrcode.image.svg.SvgImage)
            type(img)
            print("Your new QR code will be saved to the 'imgs' directory.")
            img.save(filepath)
        else:
            img = qrcode.make(qr_data)
            type(img)
            print("Your new QR code will be saved to the 'imgs' directory.")
            img.save(filepath)
                

