# usage: python demo.py

# import necessary packages
import cv2
from dataset import video, advertisements
from utils import render_advertisement, clear_advertisement

# check if video was read successfully
if video.isOpened() == False:
	raise("Error opening video")

paused = False
# read and display until video is complete
while video.isOpened():
	grabbed, frame = video.read()
	if not grabbed:
		break
	else:
		# if "spacebar" is pressed, pause and render advertisement until "spacebar" is pressed again
		if cv2.waitKey(1) & 0xFF == ord(" "):
			paused=True
			render_advertisement()
			# pause until "spacebar" is pressed again
			while paused:
				if cv2.waitKey(1) & 0xFF == ord(" "):
					paused = False
					clear_advertisement()
					break
		else:
			cv2.imshow("Video", frame)