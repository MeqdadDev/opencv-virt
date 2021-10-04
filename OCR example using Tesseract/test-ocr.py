import cv2 as cv
import pytesseract
from time import sleep

def get_ocr(img):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return pytesseract.image_to_string(rgb)
'''
img = cv.imread('numbers.jpeg')

cv.imshow('Test OCR Image', img)
text_ocr = get_ocr(img)
print('text_ocr: ', text_ocr)
cv.waitKey(0)'''

'''
def screenshot(img_frame):
    return cv.imwrite('Screenshot.jpg', img_frame)

cam = cv.VideoCapture(0)

while True:
    is_success, frame = cam.read()
    if not is_success:
        print("failed to capture image.")
        break
    cv.imshow("OCR Stream", frame)

    k = cv.waitKey(1)

    # Check if space is pressed
    if k%256 == 32:
        screenshot(frame)
        print(f"Image captured!")
        image = cv.imread('Screenshot.jpg')
        print(get_ocr(image))
    if k%256 == 27:
        print("Press ESC to close...")
        break

cv.destroyAllWindows()
'''