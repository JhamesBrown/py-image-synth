import random, time
from PIL import Image, ImageDraw

img = Image.new('RGB', (200,200), color = (255,0,0))

draw = ImageDraw.Draw(img)

for x in range(0, img.size[1]):
    rand1 = random.randint(0,img.size[0])
    rand2 = random.randint(0,img.size[0])
    draw.line((rand1,x,rand2,x), fill= (0,0,255) )
del draw

timeStamp = time.strftime('%Y%m%h')
filename = 'exp_'+timeStamp+'.png'
img.save('output/'+filename)
