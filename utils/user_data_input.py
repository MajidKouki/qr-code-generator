# Initial imports
import questionary


# Function that asks for user input and returns variables containing the answers.
def user_intake_data():
    qr_data = questionary.text("What URL, data or text do you want converted?").ask()
    filename_data = questionary.text("What should the images filename be? Include the extension (ex. Hello.png)").ask()
    return qr_data, filename_data