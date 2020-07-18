import os
import requests


# CONSTS
IMG_DIR = r"C:\Users\evoosa\Desktop\Projects\Python\BlinkRandom"
RESOLUTION = (1920, 1080)
IMG_URL = "https://loremflickr.com/{w}/{h}".format(w=RESOLUTION[0], h=RESOLUTION[1])
IMG_FILENAME = 'BlinkImage.jpeg'
IMG_PATH = os.path.join(IMG_DIR, IMG_FILENAME)

# IMPORTANT

# Download image
page = requests.get(IMG_URL)
with open(IMG_PATH, 'wb') as f:
    f.write(page.content)
