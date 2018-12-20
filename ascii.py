from PIL import Image
# the char list can be customized
ascii_char=list("-----!@#$%^&+++++")

# converting gray values to characters in the list
def getchar(r,g,b,alpha=256):
    if alpha == 0:
        return ' '
    else:
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    length = len(ascii_char)
    unit = 256/length
    return ascii_char[int(gray/unit)]
#load image 

im =Image.open(filename)

# get size

width = int(0.4*im.size[0])
height = int(0.15*im.size[1])
im = im.resize((width,height),Image.ANTIALIAS)
txt=""

# call getchar
for i in range(height):
    for j in range(width):
        txt+=getchar(*im.getpixel((j,i)))
    txt+='\n'
    
f=open('filename.txt','w')
f.write(txt)
