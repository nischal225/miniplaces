import numpy as np
import os
import scipy.misc
from scipy import ndimage
import scipy.ndimage
from random import choice, randint
from scipy.ndimage.interpolation import zoom
np.random.seed(123)


def augment_image(image):
	switch = randint(0, 3)

	if switch == 0:
		blurred_image = ndimage.uniform_filter(image, size=(7, 7, 1))
		#scipy.misc.imsave(os.path.join('./', 'image_trans/blurred.jpg'), blurred_image)
		return blurred_image
	elif switch == 1:
		zoomed_image = scipy.ndimage.filters.gaussian_filter(image, 1.5)
		#scipy.misc.imsave(os.path.join('./', 'image_trans/zoomed.jpg'), zoomed_image)
		return zoomed_image
	elif switch == 2:
		flipped_image = np.fliplr(image)
		#scipy.misc.imsave(os.path.join('./', 'image_trans/flipped.jpg'), flipped_image)
		return flipped_image
	elif switch == 3:
		rotation_angle = choice([randint(-70, -20), randint(20, 70)])
		rotated_image = scipy.ndimage.interpolation.rotate(image, rotation_angle, mode='reflect', reshape=False)
		#scipy.misc.imsave(os.path.join('./', 'image_trans/rotated.jpg'), rotated_image)
		return rotated_image
	else:
		blurred_image = ndimage.uniform_filter(image, size=(7, 7, 1))
		return blurred_image

	# elif switch == 4:
	# 	shifted_amount = choice([randint(5.0, 13.0)])
	# 	shifted_image = scipy.ndimage.interpolation.shift(image, shifted_amount, mode='reflect')
	# 	scipy.misc.imsave(os.path.join('./', 'image_trans/rotated.jpg'), shifted_image)


if __name__ == "__main__":
	parent_dir = '../../data/images/train/a/abbey/'
	im_name = '00000004.jpg'
	image_path = os.path.join(parent_dir, im_name)
	image = scipy.misc.imread(image_path)
	aug_img = augment_image(image)
# scipy.misc.imshow(image)

