from random import randint
from skimage import draw
import numpy as np
from draw_fig import draw_fig
import math

""" Does the same as triangle.py but wihtout noise (the shape is perfectly sharp) """
def draw_triangle_w_n(img, interruption, missing_fragments, difficulty, size_min, size_max, pixel_processing, rand):
  heigth = img.shape[0]
  width = img.shape[1]
  x1 = rand.randint(0, width)
  y1 = rand.randint(0, heigth)
  x2, x3, y2, y3 = -1, -1, -1, -1
  rmin = size_min
  rmax = size_max
  
  x2 = rand.randint(x1 + rmin, x1 + rmax)
  y2 = y1
    
  x3 = rand.randint(x2 - rmax, x2 - round(rmin / 2))
  y3 = rand.randint(y2 + round(rmin / 2), y2 + rmax)
  num = rand.randint(0, 2)
  angle = rand.randint(0, 180) if num == 1 else 0

  bb = []
  xmin = min(x1, x2, x3)
  ymin = min(y1, y2, y3)
  xmax = max(x1, x2, x3)
  ymax = max(y1, y2, y3)
  bb.append([x1, y1])
  bb.append([x2 ,y2])
  bb.append([x3, y3])

  row, col = draw.polygon((y1, y2, y3), (x1, x2, x3))
  points = []
  x = rand.randint(xmin, xmax)
  d = rand.randint(20, 40)

  if missing_fragments:
    j = 0
    frags = rand.randint(missing_fragments[0], missing_fragments[1] + 1)
    if frags == 0:
      for i in range(len(row)):
        x_old = col[i] - x1
        y_old = row[i] - y1
        if interruption:
          if x_old > x - x1 and x_old < x - x1 + d:
            continue
        points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x1 , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y1 ])
        if points[j][0] >= width or points[j][1] >= heigth or points[j][0] < 0 or points[j][1] < 0:
          points[j][0] = x1
          points[j][1] = y1
        j = j + 1
    if frags == 1:
      px = rand.randint(0, 1)
      x1 = xmax if px == 1 else xmin
      y1 = rand.randint(ymin, ymax)
      a1 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b1 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      for i in range(len(row)):
          if not ((col[i] - x1)**2 / a1**2 + (row[i] - y1)**2 / b1**2 < 1):
            #points.append([col[i] - x, row[i] - y])
            x_old = col[i] - x1
            y_old = row[i] - y1
            if interruption:
              if x_old > x - x1 and x_old < x - x1 + d:
                continue
            points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x1 , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y1 ])
            if points[j][0] >= width or points[j][1] >= heigth or points[j][0] < 0 or points[j][1] < 0:
              points[j][0] = 0
              points[j][1] = 0
            j = j + 1

    elif frags == 2:
      px = rand.randint(0, 1)
      py = rand.randint(0, 1)
      x1 = xmax if px == 1 else xmin
      y1 = rand.randint(ymin, ymax)
      y2 = ymax if py == 1 else ymin
      x2 = rand.randint(xmin, xmax)
      a1 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b1 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a2 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b2 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      for i in range(len(row)):
        if not ((col[i] - x1)**2 / a1**2 + (row[i] - y1)**2 / b1**2 < 1) and not((col[i] - x2)**2 / a2**2 + (row[i] - y2)**2 / b2**2 < 1):
          #points.append([col[i] - x, row[i] - y])
          x_old = col[i] - x1
          y_old = row[i] - y1
          if interruption:
            if x_old > x - x1 and x_old < x - x1 + d:
              continue
          points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x1 , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y1 ])
          if points[j][0] >= width or points[j][1] >= heigth or points[j][0] < 0 or points[j][1] < 0:
            points[j][0] = 0
            points[j][1] = 0
          j = j + 1

    elif frags == 3:
      px1 = rand.randint(0, 1)
      px3 = rand.randint(0, 1)
      py = rand.randint(0, 1)
      x1 = xmax if px1 == 1 else xmin
      y1 = rand.randint(ymin, round((ymax - ymin) / 2) + ymin)
      y2 = ymax if py == 1 else ymin
      x2 = rand.randint(xmin, xmax)
      x3 = xmax if px3 == 1 else xmin
      y3 = rand.randint(round((ymax - ymin) / 2) + ymin, ymax)
      a1 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b1 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a2 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b2 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a3 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b3 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      for i in range(len(row)):
        if not ((col[i] - x1)**2 / a1**2 + (row[i] - y1)**2 / b1**2 < 1) and not((col[i] - x2)**2 / a2**2 + (row[i] - y2)**2 / b2**2 < 1) and not ((col[i] - x3)**2 / a3**2 + (row[i] - y3)**2 / b3**2 < 1):
          #points.append([col[i] - x, row[i] - y])
          x_old = col[i] - x1
          y_old = row[i] - y1
          if interruption:
            if x_old > x - x1 and x_old < x - x1 + d:
              continue
          points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x1 , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y1 ])
          if points[j][0] >= width or points[j][1] >= heigth or points[j][0] < 0 or points[j][1] < 0:
            points[j][0] = 0
            points[j][1] = 0
          j = j + 1
      
    elif frags == 4:
      x1 = xmax
      y1 = rand.randint(ymin, round((ymax - ymin) / 2) + ymin)
      y2 = ymax
      x2 = rand.randint(xmin, xmax)
      x3 = xmax
      y3 = rand.randint(round((ymax - ymin) / 2) + ymin, ymax)
      x4 = rand.randint(xmin, xmax)
      y4 = ymin
      a1 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b1 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a2 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b2 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a3 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b3 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a4 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b4 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      for i in range(len(row)):
        if not ((col[i] - x1)**2 / a1**2 + (row[i] - y1)**2 / b1**2 < 1) and not((col[i] - x2)**2 / a2**2 + (row[i] - y2)**2 / b2**2 < 1) and not ((col[i] - x3)**2 / a3**2 + (row[i] - y3)**2 / b3**2 < 1) and not ((col[i] - x4)**2 / a4**2 + (row[i] - y4)**2 / b4**2 < 1):
          #points.append([col[i] - x, row[i] - y])
          x_old = col[i] - x1
          y_old = row[i] - y1
          if interruption:
            if x_old > x - x1 and x_old < x - x1 + d:
              continue
          points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x1 , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y1 ])
          if points[j][0] >= width or points[j][1] >= heigth or points[j][0] < 0 or points[j][1] < 0:
            points[j][0] = 0
            points[j][1] = 0
          j = j + 1
    
    elif frags == 5:
      x1 = xmax
      y1 = rand.randint(ymin, round((ymax - ymin) / 2) + ymin)
      y2 = ymax
      x2 = rand.randint(xmin, xmax)
      x3 = xmax
      y3 = rand.randint(round((ymax - ymin) / 2) + ymin, ymax)
      x4 = rand.randint(xmin, xmax)
      y4 = ymin
      x5 = xmin
      y5 = rand.randint(round((ymax - ymin) / 2) + ymin, ymax)
      a1 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b1 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a2 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b2 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a3 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b3 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a4 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b4 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a5 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b5 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      for i in range(len(row)):
        if not ((col[i] - x1)**2 / a1**2 + (row[i] - y1)**2 / b1**2 < 1) and not((col[i] - x2)**2 / a2**2 + (row[i] - y2)**2 / b2**2 < 1) and not ((col[i] - x3)**2 / a3**2 + (row[i] - y3)**2 / b3**2 < 1) and not ((col[i] - x4)**2 / a4**2 + (row[i] - y4)**2 / b4**2 < 1) and not ((col[i] - x5)**2 / a5**2 + (row[i] - y5)**2 / b5**2 < 1):
          #points.append([col[i] - x, row[i] - y])
          x_old = col[i] - x1
          y_old = row[i] - y1
          if interruption:
            if x_old > x - x1 and x_old < x - x1 + d:
              continue
          points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x1 , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y1 ])
          if points[j][0] >= width or points[j][1] >= heigth or points[j][0] < 0 or points[j][1] < 0:
            points[j][0] = 0
            points[j][1] = 0
          j = j + 1

    elif frags == 6:
      x1 = xmax
      y1 = rand.randint(ymin, round((ymax - ymin) / 2) + ymin)
      y2 = ymax
      x2 = rand.randint(xmin, xmax)
      x3 = xmax
      y3 = rand.randint(round((ymax - ymin) / 2) + ymin, ymax)
      x4 = rand.randint(xmin, xmax)
      y4 = ymin
      x5 = xmin
      y5 = rand.randint(round((ymax - ymin) / 2) + ymin, ymax)
      x6 = rand.randint(xmin, xmax)
      y6 = ymin
      a1 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b1 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a2 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b2 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a3 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b3 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a4 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b4 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a5 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b5 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      a6 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4)) + 1
      b6 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4)) + 1
      for i in range(len(row)):
        if not ((col[i] - x1)**2 / a1**2 + (row[i] - y1)**2 / b1**2 < 1) and not((col[i] - x2)**2 / a2**2 + (row[i] - y2)**2 / b2**2 < 1) and not ((col[i] - x3)**2 / a3**2 + (row[i] - y3)**2 / b3**2 < 1) and not ((col[i] - x4)**2 / a4**2 + (row[i] - y4)**2 / b4**2 < 1) and not ((col[i] - x5)**2 / a5**2 + (row[i] - y5)**2 / b5**2 < 1) and not ((col[i] - x6)**2 / a6**2 + (row[i] - y6)**2 / b6**2 < 1):
          #points.append([col[i] - x, row[i] - y])
          x_old = col[i] - x1
          y_old = row[i] - y1
          if interruption:
            if x_old > x - x1 and x_old < x - x1 + d:
              continue
          points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x1 , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y1 ])
          if points[j][0] >= width or points[j][1] >= heigth or points[j][0] < 0 or points[j][1] < 0:
            points[j][0] = 0
            points[j][1] = 0
          j = j + 1
  else:
    k = 0
    for i in range(len(row)):
      x_old = col[i] - x1
      y_old = row[i] - y1
      if interruption:
        if x_old > x - x1 and x_old < x - x1 + d:
          continue
      points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + x1 , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + y1 ])
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