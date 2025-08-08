import cv2
import numpy as np

img = cv2.imread("SMC.jpg")


# Read the same image in different modes
img_color = cv2.imread("SMC.jpg", cv2.IMREAD_COLOR)       # Color
img_gray = cv2.imread("SMC.jpg", cv2.IMREAD_GRAYSCALE)    # Grayscale
img_unchanged = cv2.imread("SMC.jpg", cv2.IMREAD_UNCHANGED)  # Unchanged

# Show images in different modes
cv2.imshow("Color Image", img_color)
cv2.imshow("Grayscale Image", img_gray)
cv2.imshow("Unchanged Image", img_unchanged)

# Flip images in different directions
flip_h = cv2.flip(img_color, 1)   # Horizontal flip
flip_v = cv2.flip(img_color, 0)   # Vertical flip
flip_both = cv2.flip(img_color, -1)  # Horizontal + Vertical flip

# Show flipped images
cv2.imshow("Flip Horizontal", flip_h)
cv2.imshow("Flip Vertical", flip_v)
cv2.imshow("Flip Both", flip_both)

rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
rotate_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Rotate 90°", rotate_90)
cv2.imshow("Rotate 180°", rotate_180)
cv2.imshow("Rotate 270°", rotate_270)


# Crop center region
# start_x, start_y = w // 4, h // 4
# end_x, end_y = start_x + w // 2, start_y + h // 2
# crop_center = img[start_y:end_y, start_x:end_x]

# # Crop top-left region
# crop_top_left = img[0:h // 2, 0:w // 2]

# # Show cropped regions
# cv2.imshow("Crop Center", crop_center)
# cv2.imshow("Crop Top Left", crop_top_left)

cv2.waitKey(0)
cv2.destroyAllWindows()

