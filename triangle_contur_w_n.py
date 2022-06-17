from random import randint
from skimage import draw
import numpy as np
from draw_fig import draw_fig
import math

""" Does the same as triangle_contur.py but wihtout noise (the shape is perfectly sharp) """
def draw_triangle_contur_w_n(img, interruption, difficulty, size_min, size_max, pixel_processing, rand):
  heigth = img.shape[0]
  width = img.shape[1]
  x1 = rand.randint(0, width)
  y1 = rand.randint(0, heigth)
  x2, x3, y2, y3 = -1, -1, -1, -1
  rmin = round(size_min / 1.5)
  rmax = round(size_max / 1.5) + 1
  
  x2 = rand.randint(x1 + rmin, x1 + rmax)
  y2 = rand.randint(y1 + rmin, y1 + rmax)
    
  x3 = rand.randint(x2 - rmax, x2 - round(rmin / 2))
  y3 = rand.randint(y2 + round(rmin / 2), y2 + rmax)
  num = rand.randint(0, 2)
  angle = rand.randint(0, 180) if num == 1 else 0

  bb = []
  xmin = min(x1, x2, x3)
  ymin = min(y1, y2, y3)
  xmax = max(x1, x2, x3)
  ymax = max(y1, y2, y3)
  if ymin < 0:
    ymin = 0
  if xmin < 0:
    xmin = 0
  if ymax >= heigth:
    ymax = heigth - 5
  if xmax >= width:
    xmax = width - 5
  bb.append([x1, y1])
  bb.append([x2 ,y2])
  bb.append([x3, y3])

  points = []
  x = rand.randint(xmin, xmax + 5)
  d = rand.randint(10, 40)
  k = 0
  for i in range(5):
    row, col = draw.polygon_perimeter((y1 - i, y2 - i, y3 - i), (x1 - i, x2 - i, x3 - i))
    for j in range(len(row)):
      x_old = col[j] - x1
      y_old = row[j] - y1
      if interruption:
          if x_old > x - x1 and x_old < x - x1 + d:
            continue
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

  xmin = min(bb[0][0], bb[1][0], bb[2][0])#, bb[3][0])
  ymin = min(bb[0][1], bb[1][1], bb[2][1])#, bb[3][1])
  xmax = max(bb[0][0], bb[1][0], bb[2][0])#, bb[3][0])
  ymax = max(bb[0][1], bb[1][1], bb[2][1])#, bb[3][1])
  bb = []
  bb.append(xmin)
  bb.append(ymin)
  bb.append(xmax)
  bb.append(ymax)
    
  img = draw_fig(img, points, bb, difficulty, pixel_processing, rand)
  return img, bb