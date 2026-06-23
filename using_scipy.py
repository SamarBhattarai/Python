import numpy as np
import scipy.signal

grayscale_image = np.zeros((10,10))
print(grayscale_image)

grayscale_image[0:5,:] = 255
print(grayscale_image)

filter = np.array([[0,1,1,0],
                   [1,3,3,1],
                   [-1,-3,-3,-1],
                   [0,-1,-1,0]])

# Note that we will use valid mode which means no padding.
convolved_image = scipy.signal.convolve2d(grayscale_image, filter, mode = "valid")
print(convolved_image)
print(type(convolved_image))

print("Resulting Feature Map (Truncated View):")
print(convolved_image[:, 0:4].astype(int))