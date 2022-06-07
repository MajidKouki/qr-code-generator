# Initial imports
import fire


# Custom imports
from utils.user_data_input import user_intake_data
from utils.qr_code_generator import qr_code_generator


# Runs the program
def run():
    qr_data, filename_data = user_intake_data()
    qr_code_generator(qr_data, filename_data)


# Run program
if __name__ == "__main__":
    fire.Fire(run)