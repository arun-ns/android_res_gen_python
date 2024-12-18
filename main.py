import os

from PIL import Image


def list_image_files_in_folder(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg',
                        '.tiff']  # Add more extensions if needed
    image_files_list = []

    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path) and os.path.splitext(file)[1].lower() in image_extensions:
                image_files_list.append(file)
    return image_files_list


def create_android_folders(output_directory):
    # Define Android DPIs and their corresponding folder names
    dpis = ["drawable-mdpi", "drawable-hdpi", "drawable-xhdpi", "drawable-xxhdpi",
            "drawable-xxxhdpi"]
    # Create output directories if they don't exist
    for dpi in dpis:
        dpi_folder = os.path.join(output_directory, dpi)
        os.makedirs(dpi_folder, exist_ok=True)


def cropAndSaveImage(file_name: str):
    # Open the PNG image
    image = Image.open(f"images/{file_name}")
    originalWeight = image.width
    originalHeight = image.height
    originalWeight = 320
    originalHeight = 320
    print(f"originalWeight {originalWeight} originalHeight : {originalHeight}")
    height = int(originalHeight / 4)
    weight = int(originalWeight / 4)
    mdpiSize = (height, weight)
    hdpiSize = (int(weight * 1.5), int(height * 1.5))
    xhdpiSize = (int(weight * 2), int(height * 2))
    xxhdpiSize = (int(weight * 3), int(height * 3))
    xxxhdpiSize = (int(weight * 4), int(height * 4))
    print(f"mdpiSize {mdpiSize}")
    # file_name = file_name.replace(".png", ".webp")
    image.resize(mdpiSize).save(f"images_cropped/drawable-mdpi/{file_name}")
    image.resize(hdpiSize).save(f"images_cropped/drawable-hdpi/{file_name}")
    image.resize(xhdpiSize).save(f"images_cropped/drawable-xhdpi/{file_name}")
    image.resize(xxhdpiSize).save(f"images_cropped/drawable-xxhdpi/{file_name}")
    image.resize(xxxhdpiSize).save(f"images_cropped/drawable-xxxhdpi/{file_name}")
    # image.save(f"images_cropped/drawable-xxxhdpi/{file_name}")
    print("DONE")




print("Start Generate resource....")
create_android_folders("images_cropped")
files = list_image_files_in_folder("images")
if files:
    print("Files in the folder:")
    for file in files:
        cropAndSaveImage(file)
        print(file)
