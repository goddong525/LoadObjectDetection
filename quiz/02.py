import cv2
import json

image=cv2.imread('../data/images/' + file_name)

f=open('../data/labels/labels.json')
labels = json.load(f)

file_name = input()
for label in labels:
    if label['name'] = file_name:
        for l in label['labels']:
            if 'box2d' in l:
                x1=int(l['box2d']['x1'])
                y1 = int(l['box2d']['y1'])
                x2 = int(l['box2d']['x2'])
                y2 = int(l['box2d']['y3'])

