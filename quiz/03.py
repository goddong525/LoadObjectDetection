import cv2
import os
import json


f = open('../data/labels/labels.json')

file_name = 'c1ba5ee6-a7916d65.jpg'
image = cv2.imread('../data/images/' + file_name)

resize_image = cv2.resize(image,(100,200))




cv2.rectangle(image, (10, 10), (100, 100), (0, 0, 255), 3)

cv2.imshow('image', image)
cv2.imshow('resize image', resize_image)

if not os.path.exists('resize_image'):
    os.mkdir('resize_image')

cv2.imwrite('resize_image/0.jpg', resize_image)

cv2.waitKey(0)