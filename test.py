from PIL import Image
 
# Opens a image in RGB mode
img = Image.open(r"/Users/maximderhachov/Desktop/img.jpg")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
height = img.size[0]
width = img.size[1]

print(f'width = {width}, height = {height}')
  
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = img.size

if width > 500:
    width -= 500
if height > 300:
    height -= 300
 
# Setting the points for cropped image
left = width / 2
top = height / 2
right = 500 + width / 2
bottom = 300 + height /2
 
# Cropped image of above dimension
# (It will not change original image)
im1 = img.crop((left, top, right, bottom))
 
# Shows the image in image viewer
im1.show()

height = im1.size[0]
width = im1.size[1]

print(f'width = {width}, height = {height}')