import os
import sys
import asyncio
import processor


images_directory = sys.argv[1]  
output_directory = sys.argv[2]
output_file_name = sys.argv[3]

output_path = output_directory + "/" + output_file_name 

async def list_files(images_directory, output_path):
    list_of_files = []

    for filename in os.listdir(images_directory):
        if os.path.isfile(os.path.join(images_directory, filename)):
            list_of_files.append(filename)

    await processor.process_document(list_of_files, images_directory, output_path)

asyncio.run(list_files(images_directory, output_path))