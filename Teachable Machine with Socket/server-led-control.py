import socket
# import YB_Pcb_Car
from time import sleep
import RPi.GPIO as GPIO

BuzzerPin = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BuzzerPin, GPIO.OUT, initial=GPIO.LOW)

ip = "192.168.1.3"  # IP of Raspberry Pi

# start server
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((ip, 8080))
serv.listen(5)
print("SERVER: started")

while True:
    # establish connection
    conn, addr = serv.accept()
    recieved_msg = ''
    print("SERVER: connection to Client established")

    # while True:
    # receive data and print
    data = conn.recv(4096).decode()
    # if not data: break
    if not data:
        sleep(1)
        # data = conn.recv(4096).decode()
    # recieved_msg += data
    recieved_msg = data
    print("Recieved: ", recieved_msg)

    if recieved_msg == 'On':
        GPIO.output(BuzzerPin, GPIO.HIGH)
    elif recieved_msg == 'Off':
        GPIO.output(BuzzerPin, GPIO.LOW)

    # send message back to client
    msg = "Working on: " + recieved_msg
    conn.send(msg.encode())

    # close connection and exit
    # conn.close()
    # break
