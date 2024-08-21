from PIL import Image
import sys
import os


def crop_and_save(input_folder, output_folder):
    if not os.path.exists(input_folder):
        sys.exit("Joe biden cant find input folder")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    print("working with input folder: " + input_folder + " output folder: " + output_folder)
    
    #print(os.listdir(input_folder))
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            #img_resized = img.resize((224,224), 0)
            width, height = img.size
            left = width - 224
            top = height -224
            right = width
            bottom = height
            img_resized = img.crop((left, top, right, bottom))
            
            output_path = os.path.join(output_folder, filename)
            img_resized.save(output_path)
            

input_folder = 'Data/Cleaned JPEG Images/Cargill Dodge 07 20 22 Plant/Images' 
output_folder = 'Data/Cleaned JPEG Images/Cargill 072022 saved corner/Images'
crop_and_save(input_folder, output_folder)
#filename = "buildings.jpg"
#with Image.open(filename) as img:
#    img.load()
#print("hello world!")