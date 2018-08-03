import cv2
import os
datapath = os.path.dirname(os.path.abspath(__file__))
datapath = datapath + "/Data"
for file in os.listdir(datapath):
  dir_name = os.path.splitext(file)[0]
  if not os.path.exists(dir_name):
    os.makedirs(dir_name)
  vidcap = cv2.VideoCapture(file)
  success,image = vidcap.read()
  count = 0
  while success:
    cv2.imwrite(datapath+"/%s/%d.jpg" %( dir_name, count), image)     # save frame as JPEG file
    success,image = vidcap.read()
    print('%s frame no : %d ',dir_name, count)
    count += 1

