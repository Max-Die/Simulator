from random import randint
from skimage import draw
import numpy as np
from draw_fig import draw_fig
import math

""" Does the same as ellipse.py but wihtout noise (so the shape is perfectly sharp) """
def draw_line_w_n(img, thickness_min, thickness_max, interruption, difficulty, size_min, size_max, pixel_processing, rand):
  heigth = img.shape[0]
  width = img.shape[1]
  xs = rand.randint(0, width - 80)
  ys = rand.randint(0, heigth)
  xe, ye = 0, 0
  xe = rand.randint(xs + size_min, xs + size_max)
  ye = rand.randint(ys + thickness_min, ys + thickness_max)
  angle = rand.randint(0, 180)

  bb = []
  xmin = xs 
  ymin = ys
  xmax = xe
  ymax = ye
  bb.append([xmin, ymin])
  bb.append([xmin ,ymax])
  bb.append([xmax, ymin])
  bb.append([xmax, ymax])

  # get coordinates belonging to the line
  row, col = draw.rectangle(start = (ys, xs), end = (ye, xe))
  points = []
  x = rand.randint(xmin + 9, xmax - 9)
  d = rand.randint(10, 40)
  k = 0
  # rotate and interrupt the line
  for i in range(len(row[0])):
    for j in range(len(col)):
      x_old = col[j][0] - xs
      y_old = row[0][i] - ys
      if interruption:
        if x_old > x - xs and x_old < x - xs + d:
          continue
      points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + xs, round(x_old * math.sin(angle) + y_old * math.cos(angle)) + ys])
      if points[k][0] >= width or points[k][1] >= heigth or points[k][0] < 0 or points[k][1] < 0:
        points[k][0] = xs
        points[k][1] = ys
      k = k + 1
  
  for i in range(len(bb)):
    bbx = bb[i][0] - xs
    bby = bb[i][1] - ys
    bb[i][0] = round(bbx * math.cos(angle) - bby * math.sin(angle)) + xs
    bb[i][1] = round(bbx * math.sin(angle) + bby * math.cos(angle)) + ys
    if bb[i][0] >= width:
      bb[i][0] = width - 5
    if bb[i][1] >= heigth:
      bb[i][1] = heigth - 5
    if bb[i][0] < 0:
      bb[i][0] = 0
    if bb[i][1] < 0:
      bb[i][1] = 0
      
  # calculate coordinates of bounding boxes
  xmin = min(bb[0][0], bb[1][0], bb[2][0], bb[3][0])
  ymin = min(bb[0][1], bb[1][1], bb[2][1], bb[3][1])
  xmax = max(bb[0][0], bb[1][0], bb[2][0], bb[3][0])
  ymax = max(bb[0][1], bb[1][1], bb[2][1], bb[3][1])
  bb = []
  bb.append(xmin)
  bb.append(ymin)
  bb.append(xmax)
  bb.append(ymax)
  

  img = draw_fig(img, points, bb, difficulty, pixel_processing, rand)

  return img, bb