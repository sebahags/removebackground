from rembg import remove
from PIL import Image

input_path = r"C:\Users\Sebastian\Desktop\projects\python\photofolders\input\bulldog.jpeg"
output_path = r"C:\Users\Sebastian\Desktop\projects\python\photofolders\output\bulldog.png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)