from random import randint
from skimage import draw
import numpy as np
from draw_fig import draw_fig
import math

""" Does the same as rectangle.py but wihtout noise (the shape is perfectly sharp) """
def draw_rectangle_w_n(img, interruption, missing_fragments, difficulty, size_min, size_max, pixel_processing, rand):
  heigth = img.shape[0]
  width = img.shape[1]
  xs = rand.randint(0, width - 80)
  ys = rand.randint(0, heigth - 80)
  xe = rand.randint(xs + size_min, xs + size_max)
  ye = rand.randint(ys + size_min, ys + size_max)
  num = rand.randint(0, 2)
  angle = rand.randint(0, 180) if num == 1 else 0

  bb = []
  xmin = xs 
  ymin = ys
  xmax = xe
  ymax = ye
  bb.append([xmin, ymin])
  bb.append([xmin ,ymax])
  bb.append([xmax, ymin])
  bb.append([xmax, ymax])

  row, col = draw.rectangle(start = (ys, xs), end = (ye, xe))
  points = []
  x = rand.randint(xmin + 4, xmax - 4)
  d = rand.randint(10, 40)
  k = 0
  if missing_fragments:
    frags = rand.randint(missing_fragments[0], missing_fragments[1] + 1)
    if frags == 0:
      for i in range(len(row[0])):
        for j in range(len(col)):
          x_old = col[j][0] - xs
          y_old = row[0][i] - ys
          if interruption:
            if x_old > x - xs and x_old < x - xs + d:
              continue
          points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + xs , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + ys ])
          if points[k][0] >= width or points[k][1] >= heigth or points[k][0] < 0 or points[k][1] < 0:
            points[k][0] = xs
            points[k][1] = ys
          k = k + 1

    if frags == 1:
      px = rand.randint(0, 1)
      x = xmax if px == 1 else xmin
      y = rand.randint(ymin, ymax)
      a = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      for i in range(len(row[0])):
        for j in range(len(col)):
          if not ((col[j][0] - x)**2 / a**2 + (row[0][i] - y)**2 / b**2 < 1):
            x_old = col[j][0] - xs
            y_old = row[0][i] - ys
            if interruption:
              if x_old > x - xs and x_old < x - xs + d:
                continue
            points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + xs , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + ys ])
            if points[k][0] >= width or points[k][1] >= heigth or points[k][0] < 0 or points[k][1] < 0:
              points[k][0] = xs
              points[k][1] = ys
            k = k + 1
    elif frags == 2:
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
      for i in range(len(row[0])):
        for j in range(len(col)):
          if not ((col[j][0] - x1)**2 / a1**2 + (row[0][i] - y1)**2 / b1**2 < 1) and not((col[j][0] - x2)**2 / a2**2 + (row[0][i] - y2)**2 / b2**2 < 1):
            x_old = col[j][0] - xs
            y_old = row[0][i] - ys
            if interruption:
              if x_old > x - xs and x_old < x - xs + d:
                continue
            points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + xs , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + ys ])
            if points[k][0] >= width or points[k][1] >= heigth or points[k][0] < 0 or points[k][1] < 0:
              points[k][0] = xs
              points[k][1] = ys
            k = k + 1
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
      a1 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b1 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a2 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b2 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      a3 = rand.randint(round((xmax - xmin) / 10), round((xmax - xmin) / 4))
      b3 = rand.randint(round((ymax - ymin) / 10), round((ymax - ymin) / 4))
      for i in range(len(row[0])):
        for j in range(len(col)):
          if not ((col[j][0] - x1)**2 / a1**2 + (row[0][i] - y1)**2 / b1**2 < 1) and not((col[j][0] - x2)**2 / a2**2 + (row[0][i] - y2)**2 / b2**2 < 1) and not ((col[j][0] - x3)**2 / a3**2 + (row[0][i] - y3)**2 / b3**2 < 1):
            x_old = col[j][0] - xs
            y_old = row[0][i] - ys
            if interruption:
              if x_old > x - xs and x_old < x - xs + d:
                continue
            points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + xs , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + ys ])
            if points[k][0] >= width or points[k][1] >= heigth or points[k][0] < 0 or points[k][1] < 0:
              points[k][0] = xs
              points[k][1] = ys
            k = k + 1
    elif frags == 4:
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
      for i in range(len(row[0])):
        for j in range(len(col)):
          if not ((col[j][0] - x1)**2 / a1**2 + (row[0][i] - y1)**2 / b1**2 < 1) and not((col[j][0] - x2)**2 / a2**2 + (row[0][i] - y2)**2 / b2**2 < 1) and not ((col[j][0] - x3)**2 / a3**2 + (row[0][i] - y3)**2 / b3**2 < 1) and not ((col[j][0] - x4)**2 / a4**2 + (row[0][i] - y4)**2 / b4**2 < 1):
            x_old = col[j][0] - xs
            y_old = row[0][i] - ys
            if interruption:
              if x_old > x - xs and x_old < x - xs + d:
                continue
            points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + xs , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + ys ])
            if points[k][0] >= width or points[k][1] >= heigth or points[k][0] < 0 or points[k][1] < 0:
              points[k][0] = xs
              points[k][1] = ys
            k = k + 1
    
    elif frags == 5:
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
      for i in range(len(row[0])):
        for j in range(len(col)):
          if not ((col[j][0] - x1)**2 / a1**2 + (row[0][i] - y1)**2 / b1**2 < 1) and not((col[j][0] - x2)**2 / a2**2 + (row[0][i] - y2)**2 / b2**2 < 1) and not ((col[j][0] - x3)**2 / a3**2 + (row[0][i] - y3)**2 / b3**2 < 1) and not ((col[j][0] - x4)**2 / a4**2 + (row[0][i] - y4)**2 / b4**2 < 1) and not ((col[j][0] - x5)**2 / a5**2 + (row[0][i] - y5)**2 / b5**2 < 1):
            x_old = col[j][0] - xs
            y_old = row[0][i] - ys
            if interruption:
              if x_old > x - xs and x_old < x - xs + d:
                continue
            points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + xs , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + ys ])
            if points[k][0] >= width or points[k][1] >= heigth or points[k][0] < 0 or points[k][1] < 0:
              points[k][0] = xs
              points[k][1] = ys
            k = k + 1
    elif frags == 6:
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
      for i in range(len(row[0])):
        for j in range(len(col)):
          if not ((col[j][0] - x1)**2 / a1**2 + (row[0][i] - y1)**2 / b1**2 < 1) and not((col[j][0] - x2)**2 / a2**2 + (row[0][i] - y2)**2 / b2**2 < 1) and not ((col[j][0] - x3)**2 / a3**2 + (row[0][i] - y3)**2 / b3**2 < 1) and not ((col[j][0] - x4)**2 / a4**2 + (row[0][i] - y4)**2 / b4**2 < 1) and not ((col[j][0] - x5)**2 / a5**2 + (row[0][i] - y5)**2 / b5**2 < 1) and not ((col[j][0] - x6)**2 / a6**2 + (row[0][i] - y6)**2 / b6**2 < 1):
            x_old = col[j][0] - xs
            y_old = row[0][i] - ys
            if interruption:
              if x_old > x - xs and x_old < x - xs + d:
                continue
            points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + xs , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + ys ])
            if points[k][0] >= width or points[k][1] >= heigth or points[k][0] < 0 or points[k][1] < 0:
              points[k][0] = xs
              points[k][1] = ys
            k = k + 1


  else:
    k = 0
    for i in range(len(row[0])):
      for j in range(len(col)):
        x_old = col[j][0] - xs
        y_old = row[0][i] - ys
        if interruption:
          if x_old > x - xs and x_old < x - xs + d:
            continue
        points.append([round(x_old * math.cos(angle) - y_old * math.sin(angle)) + xs , round(x_old * math.sin(angle) + y_old * math.cos(angle)) + ys ])
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