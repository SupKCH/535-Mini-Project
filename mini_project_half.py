import stepper_leo
from gpiozero import Button
import cv2
import sys
import time

## Initialize USB camera & QR detector
cap = cv2.VideoCapture(0)           # Initialize camera
detector = cv2.QRCodeDetector()     # Initialize QR code detector

## Pinout setup
pulse_pin = 20
direction_pin = 21
enable_pin = 16
front_limit = Button(26)
back_limit = Button(27)

## Process parameters
delay = 0.0005              # Time (s) elasped for holding each pulse
sleep_step = 0.25           # If continuous=False, we use this as wait time before next step
buffer_clear_time = 2       # This prevent too rapidly read same QR code, set to 2 secs

## Initialize belt/stepper motor control
belt = stepper_leo.stepper(pulse_pin, direction_pin, enable_pin,
                           delay, sleep_step)

def video_capture():
    global success, img
    success, img = cap.read()
    cv2.imshow("Camera", img)
    ## exit program if we press "q" on the keyboard while in camera window
    if cv2.waitKey(1) == ord("q"):
        return False
    return True

def QR_condition_control(decoded_string):
    if decoded_string == "center":
        # expect to align the object at the center of camera view
        print("** Code is not finalized, cannot align to the center yet **")
        return
    elif decoded_string == "backwardStop":
        while True:
            if back_limit.is_pressed:
                belt.backward(step=10, continuous=False)
                print("Moving the object backward until reach the limit")
                if not video_capture():
                    break
            else:
                belt.stop()
                print("The object has reached the back limit")
                break
        return
                
    elif decoded_string == "forwardStop":
        while True:
            if front_limit.is_pressed:
                belt.forward(step=10, continuous=False)
                print("Moving the object forward until reach the limit")
                if not video_capture():
                    break
            else:
                belt.stop()
                print("The object has reached the frontlimit")
                break
        return
    else:
        print("This decoded command is not yet registered")

def decode_QR(image):
    ## Detect and Decode
    decoded_command, bbox, _ = detector.detectAndDecode(image) 
    
    ## Check if there is a QRCode in the image
    if decoded_command:
        print("DECODE COMMAND: ", decoded_command)
        return decode_command

def camera_main():
    while True:
        ## Capture & Show a captured frame from USB camera
        ## If we press "q" while on camera window, it will exit the program
        if not video_capture():
            break
        
        ## Check if there is a QRCode in the image
        ## If QRcode found, return the decoded command
        command = decode_QR(img)
        if command:
            return command

def camera_alternative():
    while True:
        ## Capture & Show a captured frame from USB camera
        ## If we press "q" while on camera window, it will exit the program
        if not video_capture():
            break
        
        ## Detect and Decode
        decoded_command, bbox, _ = detector.detectAndDecode(img) 
        
        ## Check if there is a QRCode in the image
        if decoded_command:
            print("DECODE COMMAND: ", decoded_command)
            QR_condition_control(decoded_command)
            
            ## Cooldown between QR code command executions
            start_time = time.time()
            while True:
                elapsed_time = time.time() - start_time
                if not video_capture():
                    break
                if elapsed_time > buffer_clear_time:
                    break

### Only run below code when this program is execute directly, not imported as a module
if __name__ == '__main__':
    camera_main()
    sys.exit()

####### This mini project is still expected to include Web interface (Flask) ...
####### and Google Sheet API
