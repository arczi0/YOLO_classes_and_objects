import glob
import os

if os.path.isdir('annotations'):
    annotations = glob.glob("annotations/*.txt")

    with open("merged.txt", "wb") as outfile:
        for f in annotations:
            with open(f, "rb") as infile:
                outfile.write(infile.read())
    print("Files merged")
else:
    os.mkdir("annotations")
    print("Put your annotations in a directory!")

