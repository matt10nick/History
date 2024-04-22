import os
import math 
import imageeditor
import pdfgenerator
import shutil

async def process_document(list_of_files, image_directory, output_path):
    
    pages = math.ceil(len(list_of_files) / 4)
    file_index = 0

    full_path = os.path.abspath('./Template/input.html')

    for page in range(pages):

        images_left = len(list_of_files) - file_index
        images_on_page = min(images_left, 4)

        for index in range(images_on_page):

            file = list_of_files[page*4 + index]
            path = image_directory + "/" + file

            details = getName(file)

            base_file_name = "./Template/Img/image" + str(index) + ".jpg"
            txt_file_name = "./Template/Img/image" + str(index) + "date.jpg"
            imageeditor.add_text(path, base_file_name, details[0], None)
            imageeditor.add_text(path, txt_file_name, details[0], details[1])
               
            # Copy the file
            # shutil.copy2(path, tmp_file_name)


        await pdfgenerator.generate_pdf('file:///' + full_path, './Printables/page' + str(page) + '.pdf')

        file_index += images_on_page

def getName(fileName):
    description = fileName.split("-")[0]
    year = fileName.split("-")[1].split(".")[0]

    return (description, year)