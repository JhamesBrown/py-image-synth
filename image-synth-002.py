import random, time
from PIL import Image, ImageDraw, ImageFilter

"""

"""


FGColor = (200,165,000)
BGColor = (10,0,20)

img = Image.new('RGB', (200,200), color = (20,0,40))

draw = ImageDraw.Draw(img)

r = random.randint
l = draw.line

def imageSynth():
    draw.line((0,r(-200,400),200,r(-200,400)))
    l((0,r(-200,400),200,r(-200,400)),FGColor)
    return


imageSynth()

del draw

timeStamp = time.strftime('%y%m%H%M')
filename = 'exp_'+timeStamp+'.png'
img.save('output/'+filename)
