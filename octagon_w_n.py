from random import randint
from skimage import draw
import numpy as np
from draw_fig import draw_fig
import math

""" Does the same as octagon.py but wihtout noise (so the shape is perfectly sharp) """
def draw_octagon_w_n(img, difficulty, size_min, size_max, pixel_processing, rand):
  heigth = img.shape[0]
  width = img.shape[1]
  s_min = round(size_min / 2.25)
  s_max = round(size_max / 2.25)
  x1 = rand.randint(100, width - 200)
  y1 = rand.randint(100, heigth - 300)

  x2 = rand.randint(x1 + s_min, x1 + s_max)
  y2 = rand.randint(y1 - s_min, y1 + s_min)
    
  x3 = rand.randint(x2 + s_min, x2 + s_max)
  y3 = rand.randint(y2 + s_min, y2 + s_max)
    
  x4 = rand.randint(x3 - s_min, x3 + s_min)
  y4 = rand.randint(y3 + s_min, y3 + s_max)
    
  x5 = rand.randint(x4 - s_max, x4 - s_min)
  y5 = rand.randint(y4 + s_min, y4 + s_max)
      
  x6 = rand.randint(x5 - s_max, x5 - s_min)
  y6 = rand.randint(y5 - s_min, y5 + s_min)
    
  x7 = rand.randint(x6 - s_max, x6 - s_min)
  y7 = rand.randint(y6 - s_max, y6 - s_min)

  x8 = rand.randint(x7 - s_min, x7 + s_min)
  y8 = rand.randint(y7 - s_max, y7 - s_min)

  angle = rand.randint(0, 180)

  bb = []
  
  xmin = min(x1, x2, x3, x4, x5, x6, x7, x8)
  xmax = max(x1, x2, x3, x4, x5, x6, x7, x8)

  bb.append([x1, y1])
  bb.append([x2, y2])
  bb.append([x3, y3])
  bb.append([x4, y4])
  bb.append([x5, y5])
  bb.append([x6, y6])
  bb.append([x7, y7])
  bb.append([x8, y8])

  # get coordinates of pixel belonging to the octagon
  row, col = draw.polygon((y1, y2, y3, y4, y5, y6, y7, y8), (x1, x2, x3, x4, x5, x6, x7, x8))
  points = []
  k = 0
  x = rand.randint(xmin, xmax)
  d = rand.randint(10, 40)
  for i in range(len(row)):
    x_old = col[i] - x1
    y_old = row[i] - y1
    points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x1, round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y1])
    if points[k][0] >= width or points[k][1] >= heigth or points[k][0] < 0 or points[k][1] < 0:
      points[k][0] = x1
      points[k][1] = y1
    k = k + 1
  
  for i in range(len(bb)):
    bbx = bb[i][0] - x1
    bby = bb[i][1] - y1
    bb[i][0] = round(bbx * math.cos(angle) - bby * math.sin(angle)) + x1
    bb[i][1] = round(bbx * math.sin(angle) + bby * math.cos(angle)) + y1
    if bb[i][0] >= width:
      bb[i][0] = width - 5
    if bb[i][1] >= heigth:
      bb[i][1] = heigth - 5
    if bb[i][0] < 0:
      bb[i][0] = 0
    if bb[i][1] < 0:
      bb[i][1] = 0
  
  # get coordinates of the bounding box
  xmin = min(bb[0][0], bb[1][0], bb[2][0], bb[3][0], bb[4][0], bb[5][0], bb[6][0], bb[7][0])
  ymin = min(bb[0][1], bb[1][1], bb[2][1], bb[3][1], bb[4][1], bb[5][1], bb[6][1], bb[7][1])
  xmax = max(bb[0][0], bb[1][0], bb[2][0], bb[3][0], bb[4][0], bb[5][0], bb[6][0], bb[7][0])
  ymax = max(bb[0][1], bb[1][1], bb[2][1], bb[3][1], bb[4][1], bb[5][1], bb[6][1], bb[7][1])
  bb = []
  bb.append(xmin)
  bb.append(ymin)
  bb.append(xmax)
  bb.append(ymax)
    
  img = draw_fig(img, points, bb, difficulty, pixel_processing, rand)

  return img, bb