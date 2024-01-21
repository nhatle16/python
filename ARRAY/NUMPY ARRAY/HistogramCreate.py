# Creating a histogram showing the intensity

import numpy as np
import matplotlib.pyplot as plt
import skimage.data as skdata

# flatten(): NumPy method to convert to 1D array

# plt.gray(): set the colormap to gray
# plt.imshow(): display the image within Matplotlib figure
# plt.bar(): create a bar chart
# plt.hist(): create a histogram

# skdata.camera(): gray-level 'camera' image
# skdata.coffee(): colored-level 'coffee' image


def draw_histogram(image):
    '''
    draw histogram data of 8-bit grayscale image

    Args:
        image (array): a grayscale image to draw histogram for
    '''    
    # create 1D array of histogram data (maps intensities to counts)
    # 8-bit images have intensities from 0 to 255 inclusive
    # image[ image == 0].size  # size of 1d array with intensities all equal to zero
    # for all intensities 0-255 inclusive
    histogram = [image[image==intensity].size for intensity in range(256)]
    
    # draw the histogram
    print()
    plt.figure("Histogram")
    plt.bar(x=range(256), height=histogram)
    plt.xlabel("Intensity")
    plt.ylabel("Number of Pixels")
    

# # SET THE COLORMAP TO 'GRAY' AND DISPLAY IT
# image = skdata.camera()
# plt.gray()
# plt.imshow(image)

# # SET THE COLORMAP AND PRINT SIMULTANEOUSLY
# plt.imshow(image, cmap='gray', vmin=0, vmax=255)

# # COMPUTE AND DRAW THE HISTOGRAM
# draw_histogram(image)

# plt.show()

# # draw the histogram with one line 
# image = skdata.camera()     # image is a 2D array

# plt.hist(image.flatten(),bins=256)
# plt.show()

# # MODIFY THE IMAGE
# image = skdata.camera()
# plt.imshow(255-image, cmap='gray', vmin=0, vmax=255)     # reverse the color

# new_image = image.copy()
# new_image[new_image < 150] = 0      # adjust the intensity
# plt.imshow(new_image, cmap='gray', vmin=0, vmax=255)
# plt.show()

# # ADJUST THE RESOLUTION
# image = skdata.camera()
# plt.imshow(image[::5, ::5], cmap='gray', vmin=0, vmax=255)      # omit 4 columns each time
# plt.show()

# COLOR IMAGE SETTING
image = skdata.coffee()     # 3D array (400, 600, 3) , 3 : R G B
print(image.shape)
plt.imshow(image[:,:,0], vmin=0, vmax=255)
plt.show()