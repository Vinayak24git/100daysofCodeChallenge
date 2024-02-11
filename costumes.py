import sys # to access command line aurguments

from PIL import Image #to treat those files as images

images = [] # to accumulate all of these images, one at a time from command line

for arg in sys.argv[1: ]: #to add them to list after opening them
    image= Image.open(arg)
    images.append(image)
    
images[0].save (
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)