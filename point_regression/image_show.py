from PIL import Image,ImageDraw

img=Image.open('data/images/0.png')
draw=ImageDraw.Draw(img)
c=[26, 26, 72, 18, 50, 44, 41, 75, 71, 68, 71, 67]
c=[int(j) for j in c]
for i in range(0,len(c),2):
    draw.ellipse((c[i]-2, c[i+1]-2,c[i]+2,c[i+1]+2),(255,0,0))
img.show()