import cv2
import numpy as np
import tensorflow.keras
from PIL import Image, ImageOps
from rpi_socket import send_command_to_rpi


rpi_ip = '192.168.1.3'
msg = ''


def screenshot():
    global cam
    cv2.imwrite('screenshot.png', cam.read()[1])


def do_action(prediction):
    if prediction == 0:
        print('On')
        msg = 'On'
    elif prediction == 1:
        print('Off')
        msg = 'Off'
    send_command_to_rpi(rpi_ip, msg)


if __name__ == '__main__':
    np.set_printoptions(suppress=True)

    cam = cv2.VideoCapture(0)  # You can replace it with your video path

    model = tensorflow.keras.models.load_model('keras_model.h5')

    while True:
        ret, img = cam.read()

        cv2.imshow('My Camera', img)

        ch = cv2.waitKey(5)
        if ch == 27:
            break

        screenshot()

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        image = Image.open('screenshot.png')

        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        image_array = np.asarray(image)

        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        data[0] = normalized_image_array

        prediction = np.argmax(model.predict(data)[0])
        do_action(prediction)

    cv2.destroyAllWindows()
