from urllib.parse import quote
import subprocess
import time
import pyautogui
from engine.command import speak

# Update these based on your screen
voice_call_coords = (1291, 65)    # example, replace with your values
video_call_coords = (1240, 67)    # example, replace with your values

def whatsApp(mobile_no, message, flag, name):
    flag = flag.lower()

    if flag == 'message':
        encoded_message = quote(message)
    else:
        encoded_message = quote("")

    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
    full_command = f'start "" "{whatsapp_url}"'

    subprocess.run(full_command, shell=True)
    time.sleep(6)

    if flag == 'message':
        pyautogui.press('enter')
        speak(f"Message sent successfully to {name}")

    elif flag == 'call':
        pyautogui.moveTo(voice_call_coords[0], voice_call_coords[1], duration=0.5)
        pyautogui.click()
        speak(f"Calling to {name}")

    elif flag == 'video call':
        pyautogui.moveTo(video_call_coords[0], video_call_coords[1], duration=0.5)
        pyautogui.click()
        speak(f"Starting video call with {name}")
whatsApp(7061220212, "hare krishna", "message", "Sudeshna")
