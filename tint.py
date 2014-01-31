import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required=True,
                help="The path to your image")
ap.add_argument("-o", "--output", required=True,
                help="The path to output / filename")
ap.add_argument("-r", "--red", required=False,
                help="Set the ammount of red")
ap.add_argument("-g", "--green", required=False,
                help="Set the ammount of green")
ap.add_argument("-b", "--blue", required=False,
                help="Set the ammount of blue")
args = vars(ap.parse_args())

img = cv2.imread(args["source"], 1)

if img == None:
    print("{} is not a correct filepath".format(args["image"]))

xsize, ysize, channels = img.shape

for x in range(xsize):
    for y in range(ysize):
        if args["blue"]:
            img.itemset((x, y, 0), args["blue"])
        if args["green"]:
            img.itemset((x, y, 1), args["green"])
        if args["red"]:
            img.itemset((x, y, 2), args["red"])

cv2.imwrite(args["output"], img)
