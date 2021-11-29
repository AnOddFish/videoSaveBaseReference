"""

For this code to work you'll need to download the opencv library for python
You can do that by opening the commandline on windows (or the equivalent on mac) and typing "pip install opencv-python"
If that doesn't work feel free to dm me and I can try to help troubleshoot

Fair warning, this program is not well optimized yet, and improvements are more than welcome

"""

import cv2 as cv
import datetime
# defines a camera to use
# the 0 just means that it'll use the first camera available
cap = cv.VideoCapture(0)

# defines the frame size for the window to be used in the "out" variable
# in this case it's just equal to the frame size of the recording device
frame_size = (int(cap.get(3)), int(cap.get(4)))

# ensures the rec variable's scope is global to avoid scope issues
rec = False

while True:
    # ret checks if the frame was properly read (you can safely ignore this variable)
    # frame returns the number of the frame
    ret, frame = cap.read()

    # breaks from True loop when 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        print("break")
        break

    # code inside if statement runs if 'r' is pressed
    if cv.waitKey(1) & 0xFF == ord('r'):
        if not rec:
            # update the recording variable to make sure only one recording is running at a time
            rec = True
            # stores current time in the format "day-month-year-minute-second"
            currentTime = datetime.datetime.now().strftime("%d-%m-%Y-%M-%S")
            # creates a VideoWriter object that allows for the saving of a video
            out = cv.VideoWriter(f'{currentTime}.mp4', cv.VideoWriter_fourcc(*'mp4v'), 20, frame_size)
            print('rec start')
        elif rec:
            print('already recording')
    # code inside if statement runs if 'e' is pressed
    elif cv.waitKey(1) & 0xFF == ord('e'):
        if rec:
            rec = False
            # transfer everything saved in out.write(frame) into memory in the form of an Mp4
            out.release()
            print("rec end")
        elif not rec:
            print('not recording')
    elif rec:
        # save each frame of the video in short term memory
        out.write(frame)

    # create a new window named demo and display what the camera sees in it
    cv.imshow('Demo', frame)

# stops connection to the camera
cap.release()
# closes all windows opened by this program
cv.destroyAllWindows()
