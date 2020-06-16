# contains render_advertisement() and clear_advertisement()

# import necessary packages
import numpy as np 
import cv2
from dataset import advertisements

def render_advertisement():
	'''Displays a random advertisement on screen'''
	num_ads = len(advertisements)
	ad_index = np.random.randint(num_ads)

	chosen_ad = advertisements[ad_index]
	cv2.imshow("Advertisement", chosen_ad)

def clear_advertisement():
	'''Remove the advertisement from screen'''
	cv2.destroyWindow("Advertisement")

