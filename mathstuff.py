import numpy as np
import scipy as sp
import imageio as im


arr = np.array([
    [1,2,3,4],
    [2,3,4,5],
    [-1,23,3,0]
])

dt = arr[...,:1]
dt2 = arr[...,:2]
dt3 = arr[...,:3]
dt4 = arr[...,3]
dt5 = arr[2:3]
dt6 = arr[1:3]
dt7 = arr[0:2]
dt8 = arr[0:3]

print (" This is a really long string \n"
    "that lasts for multiple lines."
    " but now we forgot the return line.\n"
    "but now we did remember it."
)

# a comment
print("hello")


x = [1.1, 2, 3]
y = [4, 5, 6]
c = np.cross(x, y)



test_image = im.imread("test.png")

print("x {} cross y {} is {}".format(x,y,c))
scan_line = test_image[0]
height = test_image.shape[0]
width = test_image.shape[1]
print(test_image[0])
im.imshow(test_image)

