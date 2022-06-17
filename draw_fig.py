from random import randint
from skimage import draw
import colorsys

""" This file colours the specific pixels in an image """
def draw_fig(img, points, bb, difficulty, pixel_processing, rand):
  pp = pixel_processing[rand.randint(0, len(pixel_processing))]
  diff_min = difficulty
  diff_max = round(1.5 * difficulty)
  diff = rand.randint(diff_min, diff_max)
  diffrgb = round(diff / 2)
  num = rand.randint(0, 3) # if num <= 1 then every pixel of the figure is gets the same colour
  # colour each pixel with the same value 
  if num <= 1:
    # change the h value in the hls colour model
    if pp == "h":
      diff = 1.5 * diff
      r, g, b = img[points[0][1], points[0][0]]
      h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
      h = h + diff /100
      s = s + diff / 3 /100
      l = l + diff / 10 / 100
      r, g, b = colorsys.hls_to_rgb(h, l, s)
      for i in range(len(points)):
        img[points[i][1], points[i][0]] = [round(r * 255), round(g * 255), round(b * 255)]   

    # change the r value in the rgb colour model
    elif pp == "r":
      diff = 1.5 * diff
      colour = img[points[0][1], points[0][0]] + [diffrgb, 0, 0] 
      for i in range(len(points)):
        img[points[i][1], points[i][0]] = colour
    
    # change the g value in the rgb colour model
    elif pp == "g":
      diff = 1.5 * diff
      colour = img[points[0][1], points[0][0]] + [0, diffrgb, 0] 
      for i in range(len(points)):
        img[points[i][1], points[i][0]] = colour
    
    # change the b value in the rgb colour model
    elif pp == "b":
      diff = 1.5 * diff
      colour = img[points[0][1], points[0][0]] + [0, 0, diffrgb] 
      for i in range(len(points)):
        img[points[i][1], points[i][0]] = colour

    # change the l value in the hsl colour model (making the shape lighter)
    elif pp == "l":
      r, g, b = img[points[0][1], points[0][0]] / 255
      h, l, s = colorsys.rgb_to_hls(r, g, b)
      l = l + diff / 3 / 100
      l = 0 if l < 0 else l
      r, g, b = colorsys.hls_to_rgb(h, l, s)
      for i in range(len(points)):
        img[points[i][1], points[i][0]] = [round(r * 255), round(g * 255), round(b * 255)]

    # change the l value in the hsl colour model (making the shape darker)
    else:
      r, g, b = img[points[0][1], points[0][0]] / 255
      h, l, s = colorsys.rgb_to_hls(r, g, b)
      l = l - diff / 3 / 100
      l = 0 if l < 0 else l
      r, g, b = colorsys.hls_to_rgb(h, l, s)
      for i in range(len(points)):
        img[points[i][1], points[i][0]] = [round(r * 255), round(g * 255), round(b * 255)]
  
  # colour each pixel with a slightly different colour
  else:
    # change the h value in the hls colour model
    if pp == "h":
      diff = 1.5 * diff
      for i in range(len(points)):
        r, g, b = img[points[i][1], points[i][0]]
        h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
        h = h + diff /100
        s = s + diff / 3 /100
        l = l + diff / 10 / 100
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        img[points[i][1], points[i][0]] = [round(r * 255), round(g * 255), round(b * 255)]   

    # change the r value in the rgb colour model
    elif pp == "r":
      diff = 1.5 * diff
      for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        img[y, x] = img[y, x] + [diffrgb, 0, 0]
    
    # change the g value in the rgb colour model
    elif pp == "g":
      diff = 1.5 * diff
      for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        img[y, x] = img[y, x] + [0, diffrgb, 0]

    # change the b value in the rgb colour model
    elif pp == "b":
      diff = 1.5 * diff
      for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        img[y, x] = img[y, x] + [0, 0, diffrgb]

    # change the l value in the hsl colour model (making the shape lighter)
    elif pp == "l":
      for i in range(len(points)):
        r, g, b = img[points[i][1], points[i][0]] / 255
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        l = l + diff / 3 / 100
        l = 0 if l < 0 else l
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        img[points[i][1], points[i][0]] = [round(r * 255), round(g * 255), round(b * 255)]

    # change the l value in the hsl colour model (making the shape darker)
    else:
      for i in range(len(points)):
        r, g, b = img[points[i][1], points[i][0]] / 255
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        l = l - diff / 3 / 100
        l = 0 if l < 0 else l
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        img[points[i][1], points[i][0]] = [round(r * 255), round(g * 255), round(b * 255)]
  
  # uncomment this if you want to have bounding boxes on the images
  
  row, col = draw.rectangle_perimeter(start = (bb[1], bb[0]), end = (bb[3], bb[2]))
  for i in range(len(row)):
    if row[i] >= 1024:
      row[i] = 0
    if col[i] >= 1024:
      col[i] = 0
  img[row, col, : ] = [255, 0, 0]
  

  return img