import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'logo.png'

logoIm = Image.open( LOGO_FILENAME )
logoWidth, logoHeight = logoIm.size

os.makedirs(os.path.join('withLogo'), exist_ok=True) #creates folder titled withLogo that will work accross multiple OS


for filename in os.listdir('./originals/'): #loops through originals folder to view the contents inside
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
        or filename == LOGO_FILENAME:
        continue
    im = Image.open(os.path.join('./originals/', filename))#opens the images inside of the originals folder 
    width, height = im.size  #assigns width and height to im.size


    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:  #if picture is too big this will resize the picture to fit within the guidelines set to square_fit_size, which in this case is 300
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height) 
            width = int(SQUARE_FIT_SIZE)
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = int(SQUARE_FIT_SIZE)
        

        print('Resizing %s...' % (filename))  #when program is running it prints that it is resizing the picture
        im = im.resize((width, height))

        print('Adding logo to %s...' % (filename))  #prints that it is adding the logo to the picture 
        im.paste(logoIm, (width - logoWidth, height - logoHeight) , logoIm)

    im.save(os.path.join('withLogo', filename))  #saves the new picture with logo to the newly created directory/ folder withLogo



#TODO: Loop over all files in the working directory
#TODO: Check if file image needs to be resized
#TODO: Calculate the new width and height to resize to.
#TODO: Add the logo.
#TODO: Save chang
