from PIL import Image
ascii_char=list("-----!@#$%^&+++++")
def getchar(r,g,b,alpha=256):
    if alpha == 0:
        return ' '
    else:
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    length = len(ascii_char)
    unit = 256/length
    return ascii_char[int(gray/unit)]

im =Image.open('timg2.jpeg')
width = int(0.4*im.size[0])
height = int(0.15*im.size[1])
im = im.resize((width,height),Image.ANTIALIAS)
txt=""
for i in range(height):
    for j in range(width):
        txt+=getchar(*im.getpixel((j,i)))
    txt+='\n'
f=open('output3.txt','w')
f.write(txt)