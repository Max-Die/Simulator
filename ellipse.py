from random import randint
from skimage import draw
import numpy as np
from draw_fig import draw_fig
import math

""" This file draws an ellipse on an image. """
def draw_ellipse(img, interruption, missing_fragments, sharpness_of_edges, difficulty, size_min, size_max, pixel_processing, rand):
  heigth = img.shape[0]
  width = img.shape[1]
  sharp = sharpness_of_edges
  # generate middle point for the ellipse
  x = rand.randint(0, width)
  y = rand.randint(0, heigth)
  angle = rand.randint(0, 180)
  # generate diameters of the ellipse
  dx, dy = 1000, 0
  rmin = round(size_min)
  rmax = round(size_max)
  while(abs(dx - dy) > 100):
    dx = rand.randint(rmin, rmax)
    dy = rand.randint(rmin, rmax)
  
  # needed for bounding boxes
  xmin = x - dx
  ymin = y - dy
  xmax = x + dx
  ymax = y + dy

  # get coordinates of pixel belonging to the ellipse
  row, col = draw.ellipse(y, x, dy, dx)
  points = []
  xi = rand.randint(x - dx + 10, x + dx - 9)
  d = rand.randint(10, 40)
  j = 0
  # rotate the figure and if wanted, delete some fragments from the ellipse
  # the number of missing fragments is drawn randomly from the specified configuration
  if missing_fragments:
    frags = rand.randint(missing_fragments[0], missing_fragments[1] + 1)
    if frags == 0:
      for i in range(len(row)):
        x_old = col[i] - x
        y_old = row[i] - y
        # if interruption is active, then points in a particular band are not modified 
        if interruption:
          if x_old > xi - x and x_old < xi - x + d:
            continue
        # rotate points
        points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x + rand.randint(-sharp, sharp), round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y + rand.randint(-sharp, sharp)])
        if points[j][0] >= width or points[j][1] >= heigth or points[j][0] < 0 or points[j][1] < 0:
              points[j][0] = 0
              points[j][1] = 0
        j = j + 1

    if frags == 1:
      # get numbers for missing fragments
      px = rand.randint(0, 1)
      x1 = xmax if px == 1 else xmin
      y1 = rand.randint(ymin, ymax)
      a1 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b1 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      for i in range(len(row)):
          # all points which belong to missing fragment are not modified 
          if not ((col[i] - x1)**2 / a1**2 + (row[i] - y1)**2 / b1**2 < 1):
            x_old = col[i] - x
            y_old = row[i] - y
            # if interruption is active, then points in a particular band are not modified 
            if interruption:
              if x_old > xi - x and x_old < xi - x + d:
                continue
            # rotate points
            points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x + rand.randint(-sharp, sharp), round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y + rand.randint(-sharp, sharp)])
            # points which are out of the range of the picture are not modified
            if points[j][0] >= width or points[j][1] >= heigth or points[j][0] < 0 or points[j][1] < 0:
              points[j][0] = 0
              points[j][1] = 0
            j = j + 1

    elif frags == 2:
      # get numbers for missing fragments
      px = rand.randint(0, 1)
      py = rand.randint(0, 1)
      x1 = xmax if px == 1 else xmin
      y1 = rand.randint(ymin, ymax)
      y2 = ymax if py == 1 else ymin
      x2 = rand.randint(xmin, xmax)
      a1 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b1 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a2 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b2 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      for i in range(len(row)):
        # all points which belong to missing fragment are not modified 
        if not ((col[i] - x1)**2 / a1**2 + (row[i] - y1)**2 / b1**2 < 1) and not((col[i] - x2)**2 / a2**2 + (row[i] - y2)**2 / b2**2 < 1):
          x_old = col[i] - x
          y_old = row[i] - y 
          # if interruption is active, then points in a particular band are not modified 
          if interruption:
            if x_old > xi - x and x_old < xi - x + d:
              continue
          # rotate points
          points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x + rand.randint(-sharp, sharp), round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y + rand.randint(-sharp, sharp)])
          # points which are out of the range of the picture are not modified
          if points[j][0] >= width or points[j][1] >= heigth or points[j][0] < 0 or points[j][1] < 0:
            points[j][0] = 0
            points[j][1] = 0
          j = j + 1

    elif frags == 3:
      # get numbers for missing fragments
      px1 = rand.randint(0, 1)
      px3 = rand.randint(0, 1)
      py = rand.randint(0, 1)
      x1 = xmax if px1 == 1 else xmin
      y1 = rand.randint(ymin, round((ymax - ymin) / 2) + ymin)
      y2 = ymax if py == 1 else ymin
      x2 = rand.randint(xmin, xmax)
      x3 = xmax if px3 == 1 else xmin
      y3 = rand.randint(round((ymax - ymin) / 2) + ymin, ymax)
      a1 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b1 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a2 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b2 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a3 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b3 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      for i in range(len(row)):
        # all points which belong to missing fragment are not modified 
        if not ((col[i] - x1)**2 / a1**2 + (row[i] - y1)**2 / b1**2 < 1) and not((col[i] - x2)**2 / a2**2 + (row[i] - y2)**2 / b2**2 < 1) and not ((col[i] - x3)**2 / a3**2 + (row[i] - y3)**2 / b3**2 < 1):
          x_old = col[i] - x
          y_old = row[i] - y
          # if interruption is active, then points in a particular band are not modified 
          if interruption:
            if x_old > xi - x and x_old < xi - x + d:
              continue
          # rotate points
          points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x + rand.randint(-sharp, sharp), round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y + rand.randint(-sharp, sharp)])
          # points which are out of the range of the picture are not modified
          if points[j][0] >= width or points[j][1] >= heigth or points[j][0] < 0 or points[j][1] < 0:
            points[j][0] = 0
            points[j][1] = 0
          j = j + 1
      
    elif frags == 4:
      # get numbers for missing fragments
      x1 = xmax
      y1 = rand.randint(ymin, round((ymax - ymin) / 2) + ymin)
      y2 = ymax
      x2 = rand.randint(xmin, xmax)
      x3 = xmin
      y3 = rand.randint(round((ymax - ymin) / 2) + ymin, ymax)
      x4 = rand.randint(xmin, xmax)
      y4 = ymin
      a1 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b1 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a2 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b2 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a3 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b3 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a4 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b4 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      for i in range(len(row)):
        # all points which belong to missing fragment are not modified 
        if not ((col[i] - x1)**2 / a1**2 + (row[i] - y1)**2 / b1**2 < 1) and not((col[i] - x2)**2 / a2**2 + (row[i] - y2)**2 / b2**2 < 1) and not ((col[i] - x3)**2 / a3**2 + (row[i] - y3)**2 / b3**2 < 1) and not ((col[i] - x4)**2 / a4**2 + (row[i] - y4)**2 / b4**2 < 1):
          x_old = col[i] - x
          y_old = row[i] - y
          # if interruption is active, then points in a particular band are not modified 
          if interruption:
            if x_old > xi - x and x_old < xi - x + d:
              continue
          # rotate points
          points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x + rand.randint(-sharp, sharp), round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y + rand.randint(-sharp, sharp)])
          # points which are out of the range of the picture are not modified
          if points[j][0] >= width or points[j][1] >= heigth or points[j][0] < 0 or points[j][1] < 0:
            points[j][0] = 0
            points[j][1] = 0
          j = j + 1
    
    elif frags == 5:
      # get numbers for missing fragments
      x1 = xmax
      y1 = rand.randint(ymin, round((ymax - ymin) / 2) + ymin)
      y2 = ymax
      x2 = rand.randint(xmin, xmax)
      x3 = xmin
      y3 = rand.randint(round((ymax - ymin) / 2) + ymin, ymax)
      x4 = rand.randint(xmin, xmax)
      y4 = ymin
      x5 = xmax
      y5 = rand.randint(round((ymax - ymin) / 2) + ymin, ymax)
      a1 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b1 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a2 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b2 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a3 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b3 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a4 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b4 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a5 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b5 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      for i in range(len(row)):
        # all points which belong to missing fragment are not modified 
        if not ((col[i] - x1)**2 / a1**2 + (row[i] - y1)**2 / b1**2 < 1) and not((col[i] - x2)**2 / a2**2 + (row[i] - y2)**2 / b2**2 < 1) and not ((col[i] - x3)**2 / a3**2 + (row[i] - y3)**2 / b3**2 < 1) and not ((col[i] - x4)**2 / a4**2 + (row[i] - y4)**2 / b4**2 < 1) and not ((col[i] - x5)**2 / a5**2 + (row[i] - y5)**2 / b5**2 < 1):
          x_old = col[i] - x
          y_old = row[i] - y
          # if interruption is active, then points in a particular band are not modified 
          if interruption:
            if x_old > xi - x and x_old < xi - x + d:
              continue
          # rotate points
          points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x + rand.randint(-sharp, sharp), round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y + rand.randint(-sharp, sharp)])
          # points which are out of the range of the picture are not modified
          if points[j][0] >= width or points[j][1] >= heigth or points[j][0] < 0 or points[j][1] < 0:
            points[j][0] = 0
            points[j][1] = 0
          j = j + 1

    elif frags == 6:
      # get numbers for missing fragments
      x1 = xmax
      y1 = rand.randint(ymin, round((ymax - ymin) / 2) + ymin)
      y2 = ymax
      x2 = rand.randint(xmin, xmax)
      x3 = xmin
      y3 = rand.randint(round((ymax - ymin) / 2) + ymin, ymax)
      x4 = rand.randint(xmin, xmax)
      y4 = ymin
      x5 = xmax
      y5 = rand.randint(round((ymax - ymin) / 2) + ymin, ymax)
      x6 = rand.randint(xmin, xmax)
      y6 = ymin
      a1 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b1 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a2 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b2 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a3 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b3 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a4 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b4 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a5 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b5 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a6 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b6 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      for i in range(len(row)):
        # all points which belong to missing fragment are not modified 
        if not ((col[i] - x1)**2 / a1**2 + (row[i] - y1)**2 / b1**2 < 1) and not((col[i] - x2)**2 / a2**2 + (row[i] - y2)**2 / b2**2 < 1) and not ((col[i] - x3)**2 / a3**2 + (row[i] - y3)**2 / b3**2 < 1) and not ((col[i] - x4)**2 / a4**2 + (row[i] - y4)**2 / b4**2 < 1) and not ((col[i] - x5)**2 / a5**2 + (row[i] - y5)**2 / b5**2 < 1) and not ((col[i] - x6)**2 / a6**2 + (row[i] - y6)**2 / b6**2 < 1):
          x_old = col[i] - x
          y_old = row[i] - y
          # if interruption is active, then points in a particular band are not modified 
          if interruption:
            if x_old > xi - x and x_old < xi - x + d:
              continue
          # rotate points 
          points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x + rand.randint(-sharp, sharp), round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y + rand.randint(-sharp, sharp)])
          # points which are out of the range of the picture are not modified
          if points[j][0] >= width or points[j][1] >= heigth or points[j][0] < 0 or points[j][1] < 0:
            points[j][0] = 0
            points[j][1] = 0
          j = j + 1
      
  else:
    for i in range(len(row)):
      # if interruption is active, then points in a particular band are not modified 
      if interruption:
        if col[i] - x > xi - x and col[i] - x < xi - x + d:
          continue
      points.append([col[i] - x, row[i] - y])

  # needed for bounding box
  xl = []
  yl =[]
  xmi = 3000
  xma = 0
  ymi = 3000
  yma = 0

  # needed for bounding box
  row, col = draw.ellipse_perimeter(y, x, dy, dx)
  pointsp = []
  # calculate exact coordinates of bounding box
  for i in range(len(row)):
    pointsp.append([col[i], row[i]])
  for i in range(len(pointsp)):
    x_oldp = pointsp[i][0] - x
    y_oldp = pointsp[i][1] - y
    xp = round(x_oldp * math.cos(angle) - y_oldp * math.sin(angle)) + x
    if xp < xmi or xp > xma:
      xl.append(xp)
    yp = round(x_oldp * math.sin(angle) + y_oldp * math.cos(angle)) + y
    if yp < ymi or yp > yma:
      yl.append(yp)

  # get coordinates of the bounding box
  xmin = max(min(xl), 0)
  xmax = min(max(xl), width - 5)
  ymin = max(min(yl), 0)
  ymax = min(max(yl), heigth - 5)

  bb = []
  bb.append(xmin)
  bb.append(ymin)
  bb.append(xmax)
  bb.append(ymax)

  img = draw_fig(img, points, bb, difficulty, pixel_processing, rand)
  return img, bb