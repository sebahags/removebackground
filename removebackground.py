from rembg import remove
from PIL import Image

input_path = r""
output_path = r""

input = Image.open(input_path)
output = remove(input)
output.save(output_path)