import cv2

# Source: camera 0
cap = cv2.VideoCapture(0)

# get the video's FPS (frames per second) and frame size
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# create a VideoWriter object to write the timelapse video
out = cv2.VideoWriter('timelapse.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

# loop through the frames of the video
frame_count = 0
total = 0
while frame_count < 20:
    ret, frame = cap.read()
    if not ret:
        break
    
    # write every Nth frame (in this case, every second)
    if frame_count % fps == 0:
        out.write(frame)
        print("Wrote frame: " + str(total))
        total += 1
        
    frame_count += 1

# release the resources
cap.release()
out.release()