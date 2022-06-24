# QR Code Generator

This is a simple program that turns user data into a QR code and saves it to the 'imgs' directory. User filename with extension is also required to name the file.

---

## Technologies

This program utilizes Python as well as the following dependencies:

* [fire](https://github.com/google/python-fire) - For the command line interface and entry-point.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs.

* [qrcode](https://github.com/lincolnloop/python-qrcode) - Generation of the QR codes.

---

## Installation Guide

Before running the code, the following dependencies must be installed:

```python
pip install fire
pip install questionary
pip install qrcode[pil]
```

---

## Usage

To use this application, simply clone the repository and run **app.py**

```python
python app.py
```

The user will be prompted to enter the data to be included in the QR code and a filename with extension.

If there are no duplicates, the QR code will be created and saved in 'imgs' with the filename given.

---

## Contributors

Brought to you by Majid Kouki. You can reach me at [majidkpy@gmail.com](mailto:majidkpy@gmail.com).

---

## License

MIT
