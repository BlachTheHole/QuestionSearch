import pywhatkit as kt
import pytesseract
import numpy as np
import cv2
import pyautogui
import keyboard
import win32api
import time


print("Download tesseract-ocr from the setup file in the folder")
print("Press g to start taking a screenshot of the question")
print("Click on the left top of your question and then click on the right bottom of your question")
print("Press e to exit the program")

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# Mouse Click Setup
state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128

# Main Loop
while True:
    if keyboard.read_key() == "g":
        # take screenshot using pyautogui
        image = pyautogui.screenshot()
        # convert image to RGB format
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        # Get positions of the question
        pos = []
        while len(pos) < 2:
            a = win32api.GetKeyState(0x01)
            if a != state_left:  # Button state changed
                state_left = a
                if a < 0:
                    pos.append(pyautogui.position())

            time.sleep(0.001)
        # Crop image to the question
        img = image[pos[0].y:pos[1].y, pos[0].x:pos[1].x]
        # Convert image to text
        search_term = pytesseract.image_to_string(img)
        # Search for the text
        kt.search(search_term)

    # Exit the program
    elif keyboard.read_key() == "e":
        break

