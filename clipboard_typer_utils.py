from pynput.keyboard import Key, Controller
from PIL import ImageGrab
import time
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def type_from_clipboard(isTypeRacer=False, leaveLastChar=False, typingDelay=20, startDelay=3000):
    ''' (bool, int, int) -> None

    Converts clipboard images to text and then simulates keystrokes based on the resulting text.

    Args:
        isTypeRacer::[bool]
            If True, the converted text is processed to accommodate for Type Racer's graphical nature
        typingDelay::[int]
            The delay between keystrokes in milliseconds
        startDelay::[int]
            The delay before the actual typing starts in milliseconds
    '''
    # Get clipboard image
    print("Getting clipboard image")
    clipboardImage = __get_clipboard_image()

    # Convert clipboard image to text
    print("Converting clipboard image to text\n")
    text = pytesseract.image_to_string(clipboardImage)
    text = text.replace("\n", " ")

    # Transform text if requested
    if isTypeRacer:
        text = __transform_text(text)

    if leaveLastChar:
        text = text[:-1]

    print("*** START OF CONVERTED TEXT ***")
    print(text)
    print("*** END OF CONVERTED TEXT ***\n")

    # Begin typing sequence
    print("Starting typing sequence")
    __type_string_with_delay(
        text=text, typingDelay=typingDelay, startDelay=startDelay)


def __get_clipboard_image():
    return ImageGrab.grabclipboard()


def __transform_text(text):
    return text.replace("|", "I").replace("\\", "").replace("1", "I")


def __type_string_with_delay(text, typingDelay, startDelay):
    keyboard = Controller()
    typingDelayInSec = typingDelay / 1000
    startDelayInSec = startDelay / 1000

    # Wait for start delay (in seconds)
    print("Start delay: {}ms".format(startDelay))
    print("Delay between characters: {}ms".format(typingDelay))
    time.sleep(startDelayInSec)

    # Begin typing
    print("Typing...")

    for ch in text:
        keyboard.type(ch)
        time.sleep(typingDelayInSec)

    print("Complete! Ready for the next image!\n")
