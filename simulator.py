from random import randint
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import RandomState
from pathlib import Path
from PIL import Image
from triangle import draw_triangle
from triangle_w_n import draw_triangle_w_n
from circular_ring import draw_circular_ring
from circular_ring_w_n import draw_circular_ring_w_n
from ellipse import draw_ellipse
from ellipse_w_n import draw_ellipse_w_n
from heptagon import draw_heptagon
from heptagon_w_n import draw_heptagon_w_n
from hexagon import draw_hexagon
from hexagon_w_n import draw_hexagon_w_n
from line import draw_line
from line_w_n import draw_line_w_n
from octagon import draw_octagon
from octagon_w_n import draw_octagon_w_n
from pentagon import draw_pentagon
from pentagon_w_n import draw_pentagon_w_n
from rectangle_contur import draw_rectangle_contur
from rectangle_contur_w_n import draw_rectangle_contur_w_n
from rectangle import draw_rectangle
from rectangle_w_n import draw_rectangle_w_n
from triangle_contur import draw_triangle_contur
from triangle_contur_w_n import draw_triangle_contur_w_n
import time 
import multiprocessing

""" This file is the main file of the dataset simulator. Please read the README.txt which you can find in this directory.
    In the following lines of code you can modify how the generated figures should look like."""

"""PARAMETER"""
MIN_NUM_OF_FIG = 3                    # minimal number of figures
MAX_NUM_OF_FIG = 8                  # maximal number of figures per picture at least MIN_NUM_OF_FIG + 1
INPUT_DIR = "../../test_images"              # directory of pictures relative to this file
THICKNESS_MIN = 2                # minimal thickness of the shape "line"
THICKNESS_MAX = 10                # maximal thickness of the shape "line"
INTERRUPTION = 0                  # controls whether a shape has an interruption and is splitted in two parts
PIXEL_PROCESSING = [ "h", "l", "d"]        # controls how the pixels of a figure could be processed
SHAPES = ["circularring", "ellipse", "trianglecontur", "triangle", "rectangle","rectanglecontur", "pentagon", "line"]    # defines all shapes which could be processed into an image
MISSING_FRAGMENTS = [0,2]             # controls whether a shape has missing fragments
SHARPNESS_OF_EDGES = 1           # controls how sharp the edges of a figure are (random noise): low -> sharp edges, minimum is 1
DIFFICULTY = 13                    # controls how much a pixel is modified: low -> difficult
SIZE_MIN = 30                     # approximitely the minimum size of an edge of a figure, minimum is 30
SIZE_MAX = 120                    # approximitely the maximum size of an edge of a figure, at least SIZE_MIN + 1
NUM_PROCESSES = 6                 # number of parallel processes running 
"""PARAMETER"""

""" Function for drawing the shapes on a single png file."""
def simulator (img, min_num_of_fig, max_num_of_fig, filename, rand):
  file = open(INPUT_DIR + "/generated/txt/" + filename + ".txt", "w+")

  num_fig = rand.randint(min_num_of_fig, max_num_of_fig + 1)
  for i in range(num_fig):
    num = rand.randint(0,2) # if num == 0 then a shape without noise is drawn
    # get a random shape to draw
    fig = SHAPES[rand.randint(0, len(SHAPES))]
    if fig == "circularring":
      if num == 0:
        # draw a perfectly shaped circular ring
        img, bb = draw_circular_ring_w_n(img, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      else:
        # draw a circular ring with nois
        img, bb = draw_circular_ring(img, SHARPNESS_OF_EDGES, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      file.write(str(bb[0]) + " " + str(bb[1]) + " " + str(bb[2]) + " " + str(bb[3]) + " " + fig + " " + str(0) + "\n")

    if fig == "ellipse":
      if num == 0:
        img, bb = draw_ellipse_w_n(img, INTERRUPTION, MISSING_FRAGMENTS, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      else:
        img, bb = draw_ellipse(img, INTERRUPTION, MISSING_FRAGMENTS, SHARPNESS_OF_EDGES, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      file.write(str(bb[0]) + " " + str(bb[1]) + " " + str(bb[2]) + " " + str(bb[3]) + " " + fig + " " + str(0) + "\n")

    if fig == "trianglecontur":
      if num == 0:
        img, bb = draw_triangle_contur_w_n(img, INTERRUPTION, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      else:
        img, bb = draw_triangle_contur(img, INTERRUPTION, SHARPNESS_OF_EDGES, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      file.write(str(bb[0]) + " " + str(bb[1]) + " " + str(bb[2]) + " " + str(bb[3]) + " " + fig + " " + str(0) + "\n")
     
    if fig == "triangle":
      if num == 0:
        img, bb = draw_triangle_w_n(img, INTERRUPTION, MISSING_FRAGMENTS, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      else:
        img, bb = draw_triangle(img, INTERRUPTION, MISSING_FRAGMENTS, SHARPNESS_OF_EDGES, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      file.write(str(bb[0]) + " " + str(bb[1]) + " " + str(bb[2]) + " " + str(bb[3]) + " " + fig + " " + str(0) + "\n")

    if fig == "rectanglecontur":
      if num == 0:
        img, bb = draw_rectangle_contur_w_n(img, INTERRUPTION, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      else:
        img, bb = draw_rectangle_contur(img, INTERRUPTION, SHARPNESS_OF_EDGES, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      file.write(str(bb[0]) + " " + str(bb[1]) + " " + str(bb[2]) + " " + str(bb[3]) + " " + fig + " " + str(0) + "\n")

    if fig == "rectangle":
      if num == 0:
        img, bb = draw_rectangle_w_n(img, INTERRUPTION, MISSING_FRAGMENTS, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      else:
        img, bb = draw_rectangle(img, INTERRUPTION, MISSING_FRAGMENTS, SHARPNESS_OF_EDGES, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      file.write(str(bb[0]) + " " + str(bb[1]) + " " + str(bb[2]) + " " + str(bb[3]) + " " + fig + " " + str(0) + "\n")

    if fig == "pentagon":
      if num == 0:
        img, bb = draw_pentagon(img, SHARPNESS_OF_EDGES, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      else:
        img, bb = draw_pentagon_w_n(img, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      file.write(str(bb[0]) + " " + str(bb[1]) + " " + str(bb[2]) + " " + str(bb[3]) + " " + fig + " " + str(0) + "\n")

    if fig == "hexagon":
      if num == 0:
        img, bb = draw_hexagon(img, SHARPNESS_OF_EDGES, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      else: 
        img, bb = draw_hexagon_w_n(img, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      file.write(str(bb[0]) + " " + str(bb[1]) + " " + str(bb[2]) + " " + str(bb[3]) + " " + fig + " " + str(0) + "\n")

    if fig == "heptagon":
      if num == 0:
        img, bb = draw_heptagon(img, SHARPNESS_OF_EDGES, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      else: 
        img, bb = draw_heptagon_w_n(img, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand) 
      file.write(str(bb[0]) + " " + str(bb[1]) + " " + str(bb[2]) + " " + str(bb[3]) + " " + fig + " " + str(0) + "\n")

    if fig == "octagon":
      if num == 0:
        img, bb = draw_octagon(img, SHARPNESS_OF_EDGES, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      else:
        img, bb = draw_octagon_w_n(img, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      file.write(str(bb[0]) + " " + str(bb[1]) + " " + str(bb[2]) + " " + str(bb[3]) + " " + fig + " " + str(0) + "\n")

    if fig == "line":
      if num == 0:
        img, bb = draw_line(img, THICKNESS_MIN, THICKNESS_MAX, INTERRUPTION, SHARPNESS_OF_EDGES, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      else:
        img, bb = draw_line_w_n(img, THICKNESS_MIN, THICKNESS_MAX, INTERRUPTION, DIFFICULTY, SIZE_MIN, SIZE_MAX, PIXEL_PROCESSING, rand)
      file.write(str(bb[0]) + " " + str(bb[1]) + " " + str(bb[2]) + " " + str(bb[3]) + " " + fig + " " + str(0) + "\n")

  file.close()   
  return img

""" This function takes a path of an picture, draws the shapes and saves it."""
def image_processing(path):
  pid = multiprocessing.current_process()._identity[0]
  """ This line is important. To have different figures for each time executing this script, you have to change "pid" in the following line. 
      Change it every time you want to have new random numbers and therefore a new configuration."""
  rand = np.random.mtrand.RandomState(pid + 100)
  img = Image.open(str(path))
  print(str(path))
  if img.mode != 'RGB':
    img = img.convert('RGB')

  img = np.array(img)
  # draw the shapes
  img = simulator(img, MIN_NUM_OF_FIG, MAX_NUM_OF_FIG, str(path)[len(INPUT_DIR) + 1 : -4], rand)
  img = Image.fromarray(img)
  img.save(INPUT_DIR + "/generated/" + str(path)[len(INPUT_DIR) + 1: -4] + ".png", "png")


if __name__ == '__main__':
  # get all the png-files from the input directory
  pathlist = Path().glob(INPUT_DIR + "/*.png")
  filepath = Path(INPUT_DIR + "/generated/")
  filepath.mkdir(parents = True, exist_ok = True)
  filepath2 = Path(INPUT_DIR + "/generated/" + "txt/")
  filepath2.mkdir(parents = True, exist_ok = True)
  pathlist = list(pathlist)
  start = time.perf_counter()
  processes = []
  iterations = int(np.ceil(len(pathlist) / NUM_PROCESSES))

  #delete
  filepath3 = Path(INPUT_DIR + "/generated/" + "txt_fine/")
  filepath3.mkdir(parents = True, exist_ok = True)

  # iterate through all png files and do it (if wanted) in parallel 
  for j in range(iterations):
    for i in range(NUM_PROCESSES):
      
      # assign each process to a png file
      if j * NUM_PROCESSES + i < len(pathlist):
        p = multiprocessing.Process(target = image_processing, args = [pathlist[j * NUM_PROCESSES + i]])
        p.start()
        processes.append(p)
    
    for process in processes:
      process.join()
  
   # stop the counter
  finish = time.perf_counter()
  print("finished in " + str(finish - start) + "seconds")
