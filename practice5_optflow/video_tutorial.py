import os
import numpy as np
import cv2 # OpenCV-Python

# This tutorial code opens a video and saves the video with frame vertically flipped.
# The code also creates a named window and shows the flipped video while processing.

# Open a video
in_fpath = "../videos/vtest.mp4"
v_in = cv2.VideoCapture(in_fpath)
#v_in = cv2.VideoCapture(0)  # You can use your webcam!!

# Get the properties of the input video
width = int(v_in.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(v_in.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = v_in.get(cv2.CAP_PROP_FPS)
print("Frame width: %d\nFrame height: %d\nFPS: %f" % (width, height, fps))

# Define the codec and create VideoWriter object
out_fpath = "videos/vtest_flip.mp4"
if os.path.exists(out_fpath): os.remove(out_fpath);
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc = cv2.VideoWriter_fourcc('H', '2', '6', '4')
v_out = cv2.VideoWriter(out_fpath, fourcc, 20, (width, height))  # Set a proper fps if you don't get from the video 

# Open a named window
cv2.namedWindow('tutorial')

while(v_in.isOpened()):
    # Grab a frame
    ret, frame = v_in.read()
    if ret==True:
        # Flip the frame vertically
        frame = cv2.flip(frame, 0)
        
        # Draw the flipped frame on the window
        cv2.imshow('tutorial', frame)
        
        # Write the flipped frame
        v_out.write(frame)
        
        # Wait a key press for 60ms
        if cv2.waitKey(60) & 0xFF == ord('q'):
            break  # 'q' key to break
    else:
        break

# Close the window
cv2.destroyAllWindows()
        
# Release video devices if job is finished
v_in.release()
v_out.release()