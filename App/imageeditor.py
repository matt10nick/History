from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL.Image import Resampling
from decouple import config

height = config('HEIGHT', cast=int)
width = config('WIDTH', cast=int)

date_field_width = 500
description_field_width = 1500

def rotate_image(image_path, saved_location, degrees_to_rotate = 90):
    # Open an image file
    with Image.open(image_path) as img:
        # Get the width and height of the image
        #width, height = img.size
        #resized = img.resize((height, width))
        # Rotate the image

        rotated = img.rotate(degrees_to_rotate, resample=Resampling.NEAREST, expand=1)
        
        # Save the rotated image
        rotated.save(saved_location)


def add_text(src_path, new_path, description, date):
   
    with Image.open(src_path) as img:
        
        font = ImageFont.truetype("arial.ttf", 88)
        w = img.size[0]
        h = img.size[1]
        
        leftPosition = w//2 - description_field_width / 2         
        descriptionImage = Image.new("RGB", (description_field_width, 150), "white")
        dI = ImageDraw.Draw(descriptionImage)        
        dI.text((750, 75), description, fill="black", anchor="mm", font=font)
        
        mergedImage = Image.new("RGB", (w, h))        
        mergedImage.paste(img)
        mergedImage.paste(descriptionImage, (int(leftPosition), h - 200))
        
        if date is not None:   
            leftPosition = w//2 - date_field_width / 2
            dateImage = Image.new("RGB", (date_field_width, 150), "white")
            d = ImageDraw.Draw(dateImage)        
            d.text((date_field_width / 2, 75), date, fill="black", anchor="mm", font=font)
            
            mergedImage.paste(dateImage, (int(leftPosition), 200))            
           

        mergedImage.save(new_path)
