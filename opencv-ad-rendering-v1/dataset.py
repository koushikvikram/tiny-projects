# contains "video" and "advertisements"

# import necessary packages
import os
import cv2

# build the VideoCapture object
video_path = "./data/video/demo_video.mp4"
video = cv2.VideoCapture(video_path)

# build a list of advertisements (images)
images_path = "./data/images/"
image_list = os.listdir(images_path)
images = [cv2.imread(images_path+img) for img in image_list]
advertisements = [cv2.resize(image, (400, 400)) for image in images]