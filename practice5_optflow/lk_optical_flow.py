import cv2
import numpy as np

# In this tutorial, we find a optical flow use cv2.calcOpticalFlowPyrLK(), which use Lucas-Kanade method,
# And display as a arrows

in_fpath = "../videos/vtest.mp4"
#in_fpath = "../videos/walking.mp4"
#in_fpath = "../videos/walking2.mp4"
v_in = cv2.VideoCapture(in_fpath)

# Parameters for lucas kanade optical flow
lk_params = {'winSize' : (10,10),
             'maxLevel': 2,
             'criteria': (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)}

# Take first frame and generate grid points
ret, old_frame = v_in.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

# Set points to find optical flow
height, width = old_gray.shape  # old_gray's a 2D numpy arrays with shape [height, width]
grid_list = []
for r in range(0, height, 10):
    for c in range(0, width, 10):
        grid_list.append([[c, r]])
grid_points = np.float32(grid_list)

# For every frame, calculate LK optical flow and visualize
while True:
    ret,frame = v_in.read()
    if not ret:
        break  # No more frame -> break
    
    # calculate optical flow
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    output_points, status, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, grid_points, None, **lk_params)
    
    # Select good points
    good_new = output_points[status==1]
    good_old = grid_points[status==1]
    
    # draw the arrows
    mask = np.zeros_like(frame)
    for i,(new, old) in enumerate(zip(good_new,good_old)):
        if np.sqrt((new[0]-old[0])**2 + (new[1]-old[1])**2) > 10:
            mask = cv2.arrowedLine(mask, (old[0],old[1]), (new[0],new[1]), (0, 0, 255), 2)
    output = cv2.add(frame, mask)
        
    # Display result
    cv2.imshow("tracking", output)
    
    # Wait a key press for 60ms
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break  # 'q' key to break
        
    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    
cv2.destroyAllWindows()
v_in.release()
