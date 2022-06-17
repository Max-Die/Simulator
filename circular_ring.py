from random import randint
from skimage import draw
import numpy as np
from draw_fig import draw_fig
import math

""" This file draws a circular ring on an image. """
def draw_circular_ring(img, sharpness_of_edges, difficulty, size_min, size_max, pixel_processing, rand):
  heigth = img.shape[0]
  width = img.shape[1]
  sharp = sharpness_of_edges
  x = rand.randint(0, width)
  y = rand.randint(0, heigth)
  d = rand.randint(round(size_min/2), round(size_max/2) + 1)
  angle = rand.randint(0, 90)
  bb = []
  xmin = width
  ymin = heigth
  xmax = 0
  ymax = 0

  # get the coordinates of pixels which belong to circular ring
  row1, col1 = draw.circle_perimeter(y, x, d)
  row2, col2 = draw.circle_perimeter(y, x, d - 2)
  row3, col3 = draw.circle_perimeter(y, x, d - 4)
  row4, col4 = draw.circle_perimeter(y, x, d - 6)

  row = np.concatenate((row1, row2, row3, row4))
  col = np.concatenate((col1, col2, col3, col4))
  points = []
  for i in range(len(row)):
    points.append([col[i], row[i]])
    
  # rotate the shape and randomly (if wanted) split the circular ring in a number of fragments
  frag = rand.randint(0, 3)
  frags = [1, 2, 4]
  fragments = frags[frag]
  if fragments == 2:
    ymax = ymax + 50
    for i in range(len(points)):
      if points[i][0] < x:
        x_old = points[i][0] - x
        y_old = points[i][1] - y
        points[i][0] = round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x + rand.randint(-sharp, sharp)
        points[i][1] = round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y + rand.randint(-sharp, sharp)
      else:
        x_old = points[i][0] - x
        y_old = points[i][1] - y + randint(0, round(d/4))
        points[i][0] = round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x + rand.randint(-sharp, sharp)
        points[i][1] = round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y + rand.randint(-sharp, sharp)
      ymax = ymax if points[i][1] <= ymax else points[i][1]
      xmax = xmax if points[i][0] <= xmax else points[i][0]
      ymin = ymin if points[i][1] >= ymin else points[i][1]
      xmin = xmin if points[i][0] >= xmin else points[i][0]
      if points[i][0] >= width or points[i][1] >= heigth or points[i][0] < 0 or points[i][1] < 0:
        points[i][0] = 0
        points[i][1] = 0

  if fragments == 4:
    for i in range(len(points)):
      if points[i][0] <= x and points[i][1] < y:
        x_old = points[i][0] - x 
        y_old = points[i][1] - y
        points[i][0] = round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x + rand.randint(-sharp, sharp)
        points[i][1] = round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y + rand.randint(-sharp, sharp)
      elif points[i][0] > x and points[i][1] <= y:
        x_old = points[i][0] - x
        y_old = points[i][1] - y + rand.randint(0, round(d/4))
        points[i][0] = round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x + rand.randint(-sharp, sharp)
        points[i][1] = round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y + rand.randint(-sharp, sharp)
      elif points[i][0] >= x and points[i][1] > y:
        x_old = points[i][0] - x + rand.randint(0, round(d/6))
        y_old = points[i][1] - y 
        points[i][0] = round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x + rand.randint(-sharp, sharp)  
        points[i][1] = round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y + rand.randint(-sharp, sharp)
      elif points[i][0] < x and points[i][1] >= y:
        x_old = points[i][0] - x 
        y_old = points[i][1] - y - rand.randint(0, round(d/6))
        points[i][0] = round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x + rand.randint(-sharp, sharp)
        points[i][1] = round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y + rand.randint(-sharp, sharp) 
      ymax = ymax if points[i][1] <= ymax else points[i][1]
      xmax = xmax if points[i][0] <= xmax else points[i][0]
      ymin = ymin if points[i][1] >= ymin else points[i][1]
      xmin = xmin if points[i][0] >= xmin else points[i][0]
      if points[i][0] >= width or points[i][1] >= heigth or points[i][0] < 0 or points[i][1] < 0:
        points[i][0] = 0
        points[i][1] = 0
      
  if fragments == 1:
    xmin = x - d
    ymin = y - d
    xmax = x + d
    ymax = y + d
    for i in range(len(points)):
      if points[i][0] >= width or points[i][1] >= heigth or points[i][0] < 0 or points[i][1] < 0:
        points[i][0] = 0
        points[i][1] = 0
  if ymin < 0:
    ymin = 0
  if xmin < 0:
    xmin = 0
  if ymax >= heigth:
    ymax = heigth - 5
  if xmax >= width:
    xmax = width - 5
  
  # add points for the bounding box
  bb = []
  bb.append(xmin)
  bb.append(ymin)
  bb.append(xmax)
  bb.append(ymax)

  img = draw_fig(img, points, bb, difficulty, pixel_processing, rand)
  return img, bb