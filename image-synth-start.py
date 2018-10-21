import random, time
from PIL import Image, ImageDraw

img = Image.new('RGB', (200,200), color = (255,0,0))

draw = ImageDraw.Draw(img)


def imageSynth():
    draw.ellipse((20,20)+(30,70), (200,180,0), None, 0)
    return

imageSynth()

del draw

timeStamp = time.strftime('%y%m%H%M')
filename = 'exp_'+timeStamp+'.png'
img.save('output/'+filename)


