import random, time
from PIL import Image, ImageDraw

"""
draws a ring with horizontal line distressing
"""


FGColor = (255,165,000)
BGColor = (20,0,40)

img = Image.new('RGB', (200,200), color = (20,0,40))

draw = ImageDraw.Draw(img)

def imageSynth():
    draw.ellipse((40,40,160,160), FGColor , None , 0 )
    draw.ellipse((50,50,150,150), BGColor , None , 0 )
    for x in range(img.size[1]):
        rand1 = random.randint(0,img.size[0])
        rand2 = random.randint(0,img.size[0])
        draw.line( (rand1,x,rand2,x) , BGColor , 1)
    return


imageSynth()

del draw

timeStamp = time.strftime('%y%m%H%M')
filename = 'exp_'+timeStamp+'.png'
img.save('output/'+filename)
