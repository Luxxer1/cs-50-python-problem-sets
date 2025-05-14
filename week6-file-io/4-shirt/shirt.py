import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    valid_exts = ('.jpg', '.jpeg', '.png')
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in valid_exts:
        sys.exit("Invalid input")
    if output_ext not in valid_exts:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    if not os.path.isfile(input_path):
        sys.exit("Input does not exist")

    try:
        shirt = Image.open('shirt.png')
    except FileNotFoundError:
        sys.exit("shirt.png not found")

    with Image.open(input_path) as img:
        fitted = ImageOps.fit(img, shirt.size)
        fitted.paste(shirt, (0, 0), shirt)
        fitted.save(output_path)

if __name__ == '__main__':
    main()
