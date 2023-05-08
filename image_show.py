from PIL import Image,ImageDraw

img = Image.open('keypoint_detection_project/dataFolder/rectangelJson/P0003266__1__0___0/20.png')

draw = ImageDraw.Draw(img)

c = [12.2, 17.1, 41.0,  20.6]

for i in range(0,len(c),2):
    print(type(draw))
    print(c[i]-1,c[i+1]-1,c[i]+1,c[i+1]+1)
    draw.ellipse((c[i]-2,c[i+1]-2,c[i]+2,c[i+1]+2),(0,0,0))

img.show()

    