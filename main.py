from PIL import Image
import os

files = os.listdir("images")

input_folder = "images"
output_folder = "edited-images"

if __name__ == "__main__":
    for file in files:
        if not file.endswith(".avif"):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)

            current_image = Image.open(input_path)
            current_image = current_image.resize((500, 500))

            output_path_avif = (os.path.splitext(output_path))[0] + ".webp"  # creates tuple with file name & extension
            current_image.save(output_path_avif, format="webp")




