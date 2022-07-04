This README.txt aims to explain the architecture and logic of the dataset simulator.
The file txt_to_xml.py takes txt files and converts them to xml files (so that you can create tfrecord files for object detection)
The simulator should work for each picture size (above 100x100 px), but is not tested for sizes other than 640x640 and 1024x1024.
It takes all png files in the directory (specified by INPUT_DIR) and modifies them. 
The modified pictures are generated in a subdirectory of INPUT_DIR, called generated. 
In the directory generated, there will be a directory called txt created, in which the metadatas of the images are stored. 
ALL PRIMARLY CONFIGURATIONS can be made by editing the simulator.py file.
You can configure the number of shapes in a picture, the sizes of the shapes, the sharpness of the shapes and the drawing style. 

If you want to do so you have to configure the simulator.py file (lines 31 - 48): 

"""PARAMETER"""
MIN_NUM_OF_FIG = 8                                      # minimal number of figures in an image
MAX_NUM_OF_FIG = 13                                     # maximal number of figures per picture
INPUT_DIR = "../pictures640"                            # directory of pictures relative to this file
THICKNESS_MIN = 8                                       # minimal thickness of the shape "line"
THICKNESS_MAX = 13                                      # maximal thickness of the shape "line"
INTERRUPTION = 0                                        # controls whether a shape has an interruption and is splitted in two parts
PIXEL_PROCESSING = ["r", "g", "b", "d", "l" "h"]        # controls how the pixels of a figure could be processed
SHAPES = ["circularring", "ellipse", "trianglecontur", "triangle", "rectanglecontur", "rectangle", "pentagon", "hexagon", "heptagon", "octagon", "line"]    # defines all shapes which could be processed into an image
#SHAPES = ["circularring", "ellipse", "trianglecontur", "triangle", "rectanglecontur", "rectangle", "line"]    # defines all shapes which could be processed into an image
MISSING_FRAGMENTS = [0, 2]                              # controls whether a shape has missing fragments
SHARPNESS_OF_EDGES = 1                                  # controls how sharp the edges of a figure are (random noise): low -> sharp edges, minimum is 1
DIFFICULTY = 15                                         # controls how much a pixel is modified: low -> difficult
SIZE_MIN = 20                                           # approximitely the minimum size of an edge of a figure, minimum is 30
SIZE_MAX = 22                                           # approximitely the maximum size of an edge of a figure, at least SIZE_MIN + 1
NUM_PROCESSES = 6                                       # number of parallel processes running 
"""PARAMETER"""

The simulator is pseudorandom, if you want to get different pictures (while having the same training configuration) please change the number in 
rand = np.random.mtrand.RandomState(pid + 100) (line 161 in simulator.py) to whatever number you want. Do this every time you want to have different results.

Additional information: 
MIN_NUM_OF_FIG: must be bigger or equal to 0

MAX_NUM_OF_FIG: must be bigger than MIN_NUM_OF_FIG

INPUT_DIR: relative path to the directory containing the png files

THICKNESS_MIN: at least 1

THICKNESS_MAX: at least THICKNESS_MIN + 1

INTERRUPTION:   0: no interruption in an figure
                1: interruption in an figure

PIXEL_PROCESSING:       r: increases the r value in rgb colour model
                        g: increases the g value in rgb colour model
                        b: increases the b value in rgb colour model
                        d: decrease the l value in hls colour model so that the figure gets darker
                        l: increase the l value in hls colour model so that the figure gets lighter
                        h: increase the h value in hls colour model

SHAPES: must be an array containing at least one of the following shapes:   circular ring 
                                                                            ellipse
                                                                            triangle contur
                                                                            triangle
                                                                            rectangle contur 
                                                                            rectangle
                                                                            pentagon
                                                                            hexagon
                                                                            heptagon
                                                                            octagon
                                                                            line (thin rectangle)

MISSING_FRAGMENTS:  must be an array containing numbers [low, high]
                    if no missing fragments are wanted then configure low = high = 0
                    otherwise high >= low + 1 and high <= 6 and low >= 0
                    only works on the figures ellipse, triangle, rectangle
                    there will be at least *low* and at most *high* missing fragments


SHARPNESS_OF_EDGES: each pixel will be moved randomly in x and y direction about a random value in {-SHARPNESS_OF_EDGES, +SHARPNESS_OF_EDGES}
                    no matter this configuration, perfectly sharp figures will always be drawn
                    the minimum value for this setting is 1

DIFFICULTY: configures how much the pixel will be processed, for example DIFFICULTY = 15 means that the r or g or b etc. value will be changed by about 15

SIZE_MIN:   SIZE_MIN is approximitely the minimum diameter of ellipse and circular ring
            each edge of another figure will be at least approximitely SIZE_MIN

SIZE_MAX:   SIZE_Max is approximitely the maximum diameter of ellipse and circular ring
            each edge of another figures will be at most approximitely SIZE_MAX
            if you are not drawing the shapes pentagon, hexagon, heptagon, octagon then SIZE_MAX >= SIZE_MIN + 1
            if you are drawing the shapes pentagon, hexagon, heptagon, octagon then SIZE_MAX >= SIZE_MIN + 2


OTHER FILES:
each file from  ellipse_w_n.py, ellipse.py, triangle_contur.py, triangle_contur_w_n.py, triangle_w_n.py, triangle.py, circular_ring_w_n.py, circular_ring.py, 
                rectangle_contur.py, rectangle_contur_w_n.py, rectangle_w_n.py, rectangle.py, pentagon.py, hexagon.py, heptagon.py, octagon.py
    has the same architecture:
                                    1. generate the coordinates of the middle point or the edges
                                    2. generate the points containing to overall shape
                                    3. rotate shape and do the missing fragments etc. 
                                    4. generate bounding boxes for shape 
                                    5. draw it with the draw_fig.py file 
    The files with ..._w_n.py (w_n = without noise) are responsible for drawing shapes with perfect shapes.
    Only the ellipse.py is documented detailed (because of similar structure to the other files).

draw_fig.py colours the pixels of the given array.
If you want to draw bounding boxes aroung a figure, you can specify this in draw_fig.py in lines 127 - 135.

The logic of the program is simple. Because of this the program can be modified easily, especially the draw_fig.py file which is responsible for colouring. 
To change the shapes of the figures, take a look at the ellipse.py file so you understand the logic.

You can run the simulator by running "python3 simulator.py" in the command line.








