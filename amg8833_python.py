import serial
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2

# configure the serial port
ser = serial.Serial('COM26', 9600, timeout=1)
time.sleep(2)
signal = b"0"
# send the signal to Arduino via serial communication
ser.write(signal)
print("Signal sent successfully!")
# wait for a moment to receive the response from Arduino
time.sleep(0.1)
img_path = 'test_img/frame_.png'
fig = plt.figure()
window_name = "my"
cv2.namedWindow(window_name)
ser.close()
ser = serial.Serial('COM26', 9600, timeout=1)
time.sleep(2)
while(1):
    # read the response from Arduino
    response = ser.readline().decode().strip()
    # print("Response from Arduino: " + response)
    arr = np.array(response.split(',')[:-1],dtype='float32')
    try :
        print(arr)
        arr = arr.reshape(8,8)
        plt.imshow(arr, cmap='hot', interpolation='nearest')
        plt.colorbar()
        plt.clim(30, 50)
        plt.savefig(img_path)
        plt.clf()  # Clear the plot for the next frame
        # plt.pause(1)
        img = cv2.imread(img_path)
        cv2.imshow(window_name,img)
        key = cv2.waitKey(1)
        if key == 27:
            break
    except:
        pass
ser.close()

